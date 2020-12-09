import math
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.AffixSelector import AffixSelector
from flexpy.Corpus import Corpus
from flexpy.CorpusAnalysis import collocator_separating_target_and_collocate_terms
from flexpy.FormGrouping import group_wordforms, get_form_group_last_morpheme_gloss
from flexpy.Text import Text
from flexpy.WordForm import WordForm, WordFormMorpheme

from flexpy.language_data.BonguData import bongu_agreement_affixes

# TODO need to be able to handle allomorphy! need to get the citation form of each morph when constructing WordForm, add self.citation_forms in addition to self.forms
# TODO try distance cutoff, don't count pronouns that are too far away
# TODO try exponential decay for distance, making a collocation weighted by closeness in time

# constants
NAN = np.nan
PRONOUN_POS_STR = "Pronoun"
PRONOUN_GLOSS_REGEX = r"^[123].*"  # don't include "pronouns" like "alone" or "emph"
AGREE_STR = "<Agree>"  # make sure these aren't confusable as words from the corpus (in collocation printouts)
DISAGREE_STR = "<Disagree>"


class TargetAffixMorpheme:
    def __init__(self, morph, affix):
        assert type(morph) is WordFormMorpheme, morph
        assert type(affix) is AffixSelector
        self.morph = morph
        self.affix = affix

    def is_syncretic_for_person(self):
        return self.affix.is_syncretic_for_person()

    def is_syncretic_for_number(self):
        return self.affix.is_syncretic_for_number()

    def is_syncretic(self):
        return self.affix.is_syncretic()

    def __repr__(self):
        return "<TargetAffixMorpheme morph={} affix={}>".format(self.morph, self.affix)


class TargetAffixMorphemeCollection:
    def __init__(self):
        self.by_morph = {}
        self.by_gloss = {}

    def add_morpheme(self, target_affix_morpheme):
        morph = target_affix_morpheme.morph
        assert type(morph) is WordFormMorpheme, morph
        assert morph not in self.by_morph, "repeat morph {}".format(morph)
        self.by_morph[morph] = target_affix_morpheme
        gloss = morph.gloss
        assert gloss not in self.by_gloss, "repeat morph gloss {} in morph {}:\n{}".format(gloss, morph, self.by_gloss)
        self.by_gloss[gloss] = target_affix_morpheme

    def get_morphemes(self):
        return list(self.by_morph.values())

    def __getitem__(self, index):
        assert type(index) is WordFormMorpheme, index
        return self.by_morph[index]


def get_syncretic_and_non_syncretic_affixes(input_affixes, verbose=False):
    syncretic_affixes = [a for a in input_affixes if a.is_syncretic()]
    non_syncretic_affixes = [a for a in input_affixes if not a.is_syncretic()]

    if verbose:
        print("\n-- syncretic affixes:")
        for x in syncretic_affixes:
            print(x)
        print("\n-- non-syncretic affixes:")
        for x in non_syncretic_affixes:
            print(x)

    return syncretic_affixes, non_syncretic_affixes


def get_all_final_morphemes_in_corpus(wordform_contents, verbose=False):
    all_wordforms = set()
    for text in wordform_contents:
        for wf in text:
            assert type(wf) is WordForm, wf
            all_wordforms.add(wf)
    final_morphemes = set()
    for wf in all_wordforms:
        # final_morpheme = get_form_group_last_morpheme(wf)
        final_morpheme = wf.morphemes[-1]
        final_morphemes.add(final_morpheme)
    final_morphemes = sorted(final_morphemes, key=repr)

    if verbose:
        print("\n-- all word-final morphemes in corpus")
        for x in final_morphemes:
            print(x)

    return final_morphemes


def get_target_affix_morpheme_collection(morphemes, affixes, verbose=False):
    target_affix_morpheme_collection = TargetAffixMorphemeCollection()
    for morph in final_morphemes:
        matches = [a for a in bongu_agreement_affixes if a.matches_morpheme(morph)]
        if len(matches) == 0:
            continue
        assert len(matches) == 1, "more than one match for morph {}: {}".format(morph, matches)
        affix = matches[0]
        if verbose:
            print("morph: {}, affix: {}".format(morph, affix))
        target_affix_morpheme = TargetAffixMorpheme(morph, affix)
        target_affix_morpheme_collection.add_morpheme(target_affix_morpheme)
    if verbose:
        print("\n-- all target affix morphemes:")
        for x in target_affix_morpheme_collection.get_morphemes():
            print("target affix morpheme: {}".format(x))
    return target_affix_morpheme_collection


def get_nearest_pronoun_offset_positions(target_affix_morpheme_collection, wordform_contents, restrict_to_agree=True):
    # TODO: clean this up (without breaking it) if have time

    # restrict collocates to pronouns only
    # for all tokens of this morpheme, get nearest pronoun
    # then create stats/histogram about those pronoun locations
    assert type(target_affix_morpheme_collection) is TargetAffixMorphemeCollection
    offset_positions = {}
    for target_affix_morpheme in target_affix_morpheme_collection.get_morphemes():
        agreement_morpheme = target_affix_morpheme.morph
        assert type(agreement_morpheme) is WordFormMorpheme, agreement_morpheme
        wf_is_target = lambda wf: wf.morphemes[-1] == agreement_morpheme
        assert agreement_morpheme not in offset_positions, "duplicate morph {}".format(agreement_morpheme)
        offset_positions[agreement_morpheme] = {}
        for text in wordform_contents:
            for wf_i in range(len(text)):
                if wf_is_target(text[wf_i]):
                    wf = text[wf_i]
                    left_context = text[:wf_i]
                    right_context = text[wf_i+1:]

                    # get nearest left pronoun and offset
                    for left_j, left_wf in enumerate(left_context[::-1]):
                        if left_wf.contains_pos(PRONOUN_POS_STR):
                            pronoun_morphs = left_wf.get_morphemes_by_pos(PRONOUN_POS_STR, gloss_regex=PRONOUN_GLOSS_REGEX, max_results=1)
                            if len(pronoun_morphs) == 0:
                                continue  # don't count this one, it was a spurious pronoun
                            pronoun_morph = pronoun_morphs[0]
                            if restrict_to_agree and (not pronoun_and_suffix_agree(pronoun_morph, agreement_morpheme)):
                                # if we are only looking at agreeing pronouns, don't let a disagreeing one stop us; ignore it
                                continue
                            offset_position = -1 * (left_j + 1)  # left_j=0 is first element left of target, thus offset is -1
                            if offset_position not in offset_positions[agreement_morpheme]:
                                offset_positions[agreement_morpheme][offset_position] = []
                            offset_positions[agreement_morpheme][offset_position].append(pronoun_morph)
                            break  # only do the nearest one
                    # simil nearest right
                    for right_j, right_wf in enumerate(right_context):
                        if right_wf.contains_pos(PRONOUN_POS_STR):
                            pronoun_morphs = right_wf.get_morphemes_by_pos(PRONOUN_POS_STR, gloss_regex=PRONOUN_GLOSS_REGEX, max_results=1)
                            if len(pronoun_morphs) == 0:
                                continue  # don't count this one, it was a spurious pronoun
                            pronoun_morph = pronoun_morphs[0]
                            if restrict_to_agree and (not pronoun_and_suffix_agree(pronoun_morph, agreement_morpheme)):
                                # if we are only looking at agreeing pronouns, don't let a disagreeing one stop us; ignore it
                                continue
                            offset_position = 1 + right_j  # right_j=0 is first element right, so offset is +1
                            if offset_position not in offset_positions[agreement_morpheme]:
                                offset_positions[agreement_morpheme][offset_position] = []
                            offset_positions[agreement_morpheme][offset_position].append(pronoun_morph)
                            break  # only do the nearest one
    return offset_positions


def get_agree_disagree_counts(target_affix_morpheme_collection, offset_positions, verbose=False):
    agree_disagree_counts = {}
    for target_affix_morpheme in target_affix_morpheme_collection.get_morphemes():
        suffix_morph = target_affix_morpheme.morph
        if verbose:
            print("\n-- suffix morph: {}".format(suffix_morph))
        suffix_gloss = suffix_morph.gloss
        agree_disagree_counts[suffix_morph] = {}
        for offset_position, pronouns in sorted(offset_positions[suffix_morph].items()):
            agree_count = 0
            disagree_count = 0
            pronoun_glosses = []
            for pronoun_morph in pronouns:
                agrees = pronoun_and_suffix_agree(pronoun_morph, suffix_morph)
                this_agree_str = AGREE_STR if agrees else DISAGREE_STR
                pronoun_glosses.append("{} ({})".format(pronoun_morph.gloss, this_agree_str))
                if agrees:
                    agree_count += 1
                else:
                    disagree_count += 1
            agree_disagree_counts[suffix_morph][offset_position] = {0: disagree_count, 1: agree_count}
            if verbose:
                print("offset {}: {}".format(offset_position, sorted(pronoun_glosses)))
    return agree_disagree_counts


def plot_agree_disagree_counts_by_morpheme(target_affix_morpheme_collection, agree_disagree_counts):
    for target_affix_morpheme in target_affix_morpheme_collection.get_morphemes():
        # plot stacked bar by offset
        suffix_morph = target_affix_morpheme.morph
        suffix_gloss = suffix_morph.gloss
        recorded_offsets = agree_disagree_counts[suffix_morph].keys()
        if len(recorded_offsets) == 0:
            # will just be empty plot
            min_offset = 0
            max_offset = 1
        else:
            min_offset = min(recorded_offsets)
            max_offset = max(recorded_offsets)
        xs = list(range(min_offset, max_offset+1))
        agree_counts = [agree_disagree_counts[suffix_morph][offset][1] if offset in agree_disagree_counts[suffix_morph] else 0 for offset in xs]
        disagree_counts = [agree_disagree_counts[suffix_morph][offset][0] if offset in agree_disagree_counts[suffix_morph] else 0 for offset in xs]
        agree_offsets = []
        disagree_offsets = []
        for offset, agree_count, disagree_count in zip(xs, agree_counts, disagree_counts):
            agree_offsets += [offset] * agree_count
            disagree_offsets += [offset] * disagree_count
        agree_offset_mean = np.mean(agree_offsets)
        disagree_offset_mean = np.mean(disagree_offsets)
        agree_offset_stdev = np.std(agree_offsets)
        disagree_offset_stdev = np.std(disagree_offsets)
        agree_num_text = "{:.1f} ({:.1f})".format(agree_offset_mean, agree_offset_stdev)
        disagree_num_text = "{:.1f} ({:.1f})".format(disagree_offset_mean, disagree_offset_stdev)
        width = 0.5

        p1 = plt.bar(xs, agree_counts, width, color="blue", label="{} {}".format(AGREE_STR, agree_num_text))
        if len(disagree_offsets) > 0:
            p2 = plt.bar(xs, disagree_counts, width, bottom=agree_counts, color="red", label="{} {}".format(DISAGREE_STR, disagree_num_text))
        plt.legend()
        syncretism_bool = target_affix_morpheme_collection[suffix_morph].is_syncretic()
        plt.title("{} syncretic={}".format(suffix_gloss, syncretism_bool))
        plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/{}_syncretic_{}.png".format(suffix_gloss.replace("/","|"), syncretism_bool))
        plt.gcf().clear()


def plot_agree_disagree_counts_by_syncretism(target_affix_morpheme_collection, agree_disagree_counts):
    # make stacked bar for all syncretic versus all non-syncretic
    for syncretism_bool in [True, False]:
        suffixes_of_this_syncretism = [target_affix_morpheme.morph for target_affix_morpheme in target_affix_morpheme_collection.get_morphemes() if target_affix_morpheme.is_syncretic() is syncretism_bool]
        agree_counts_by_offset = {}
        disagree_counts_by_offset = {}
        for suffix_morph in suffixes_of_this_syncretism:
            for offset in agree_disagree_counts[suffix_morph]:
                if offset not in agree_counts_by_offset:
                    agree_counts_by_offset[offset] = 0
                if offset not in disagree_counts_by_offset:
                    disagree_counts_by_offset[offset] = 0
                agree_counts_by_offset[offset] += agree_disagree_counts[suffix_morph][offset][1]
                disagree_counts_by_offset[offset] += agree_disagree_counts[suffix_morph][offset][0]

        # for this whole syncretism bool, make plot
        min_offset = min(min(agree_counts_by_offset.keys()), min(disagree_counts_by_offset.keys()))
        max_offset = max(max(agree_counts_by_offset.keys()), max(disagree_counts_by_offset.keys()))
        xs = list(range(min_offset, max_offset+1))
        agree_counts = [agree_counts_by_offset[offset] if offset in agree_counts_by_offset else 0 for offset in xs]
        disagree_counts = [disagree_counts_by_offset[offset] if offset in disagree_counts_by_offset else 0 for offset in xs]
        agree_offsets = []
        disagree_offsets = []
        for offset, agree_count, disagree_count in zip(xs, agree_counts, disagree_counts):
            agree_offsets += [offset] * agree_count
            disagree_offsets += [offset] * disagree_count
        agree_offset_mean = np.mean(agree_offsets)
        disagree_offset_mean = np.mean(disagree_offsets)
        agree_offset_stdev = np.std(agree_offsets)
        disagree_offset_stdev = np.std(disagree_offsets)
        agree_num_text = "{:.1f} ({:.1f})".format(agree_offset_mean, agree_offset_stdev)
        disagree_num_text = "{:.1f} ({:.1f})".format(disagree_offset_mean, disagree_offset_stdev)
        width = 0.5

        p1 = plt.bar(xs, agree_counts, width, color="blue", label="{} {}".format(AGREE_STR, agree_num_text))
        if len(disagree_offsets) > 0:
            p2 = plt.bar(xs, disagree_counts, width, bottom=agree_counts, color="red", label="{} {}".format(DISAGREE_STR, disagree_num_text))
        plt.legend()
        plt.title("all syncretic={}".format(syncretism_bool))
        plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/all_syncretism_{}.png".format(syncretism_bool))
        plt.gcf().clear()


def report_affix_collocations(target_affix_morpheme_collection, wordform_contents, 
        make_plots, restrict_to_agree,
    ):
    affix_morphemes = target_affix_morpheme_collection.get_morphemes()
    metrics = ["MI", "T"]
    spans = list(range(1, 11))
    trajectories = {}
    for affix_morpheme in affix_morphemes:
        target = affix_morpheme.morph.gloss
        morph_form = affix_morpheme.morph.citation_form
        print("\n----\nnext target: {}".format(target))
        is_syncretic = affix_morpheme.is_syncretic()
        is_syncretic_for_person = affix_morpheme.is_syncretic_for_person()
        is_syncretic_for_number = affix_morpheme.is_syncretic_for_number()

        target_grouping_function = get_form_group_last_morpheme_gloss
        # the collocates are grouped DIFFERENTLY for each affix!
        # based on whether they agree/disagree
        # so need to remake this function and thus also the corpus in collocate terms
        # make lambda closure such that resulting function has only one arg, by filling certain kwargs
        collocate_grouping_function = lambda wf: get_form_group_agree_disagree_with_affix(
            wf, affix=affix_morpheme, restrict_to_agree=restrict_to_agree,
        )
        corpus_in_target_terms = group_wordforms(wordform_contents, target_grouping_function)
        corpus_in_collocate_terms = group_wordforms(wordform_contents, collocate_grouping_function)

        mi_agree_series = []
        mi_disagree_series = []
        t_agree_series = []
        t_disagree_series = []

        for span in spans:
            for metric in metrics:
                print("next metric: {}".format(metric))
                collocates = collocator_separating_target_and_collocate_terms(
                    corpus_in_target_terms,
                    corpus_in_collocate_terms,
                    target, left=span, right=span, stat=metric, cutoff=3, ignore=[],
                )
                print("----\nCollocations for {} (syncretism {}, person {}, number {}) with span {}, using stat={}:".format(
                    target, is_syncretic, is_syncretic_for_person, is_syncretic_for_number, span, metric)
                )
                metric_agree = collocates.get(AGREE_STR, NAN)
                metric_disagree = collocates.get(DISAGREE_STR, NAN)
                if metric == "MI":
                    mi_agree_series.append(metric_agree)
                    mi_disagree_series.append(metric_disagree)
                elif metric == "T":
                    t_agree_series.append(metric_agree)
                    t_disagree_series.append(metric_disagree)
                else:
                    raise Exception("no series for metric {}".format(metric))

                print("metric[{}] = {}".format(AGREE_STR, metric_agree))
                if not restrict_to_agree:
                    print("metric[{}] = {}".format(DISAGREE_STR, metric_disagree))
                    delta = metric_agree - metric_disagree
                    ratio = metric_agree / metric_disagree if metric_disagree != 0 else NAN
                    print("delta-metric = {}; ratio-metric = {}".format(delta, ratio))
                # ct.head(collocates, hits=10)

        # save these trajectories for the big plot of all suffixes
        assert target not in trajectories, "duplicate target {}".format(target)
        trajectories[target] = {
            "mi_agree": mi_agree_series,
            "mi_disagree": mi_disagree_series,
            "t_agree": t_agree_series,
            "t_disagree": t_disagree_series,
            "is_syncretic": is_syncretic,
            "is_syncretic_for_person": is_syncretic_for_person,
            "is_syncretic_for_number": is_syncretic_for_number,
        }

        if make_plots:
            # now, for this suffix, show plot of how the metrics change with span
            if not restrict_to_agree:
                plt.subplot(2, 1, 1)

            plt.plot(spans, mi_agree_series, c="b", label="MI agree")
            plt.plot(spans, t_agree_series, c="g", label="T agree")

            if not restrict_to_agree:
                plt.plot(spans, mi_disagree_series, c="r", label="MI disagree")
                plt.plot(spans, t_disagree_series, c="m", label="T disagree")

            # also do scatter points since lines won't show up if there are nans next to a point
            plt.scatter(spans, mi_agree_series, c="k")
            plt.scatter(spans, t_agree_series, c="k")
            if not restrict_to_agree:
                plt.scatter(spans, mi_disagree_series, c="k")
                plt.scatter(spans, t_disagree_series, c="k")

            plt.legend()
            plt.title("{} ({}), syncretic={}, syn_person={}, syn_number={}".format(
                target, morph_form, is_syncretic, is_syncretic_for_person, is_syncretic_for_number,
            ))
            plt.ylabel("metric value")
            plt.xlim(min(spans)-0.5, max(spans)+0.5)  # force the x-axis to show all spans even if some have nan

            if not restrict_to_agree:
                plt.subplot(2, 1, 2)
                # show how the differences in the metrics (agree-disagree) evolve with span
                mi_diff_series = [x-y for x, y in zip(mi_agree_series, mi_disagree_series)]
                t_diff_series = [x-y for x, y in zip(t_agree_series, t_disagree_series)]
                plt.plot(spans, mi_diff_series, c="b", label="MI diff")
                plt.plot(spans, t_diff_series, c="g", label="T diff")
                # again, scatter in case of nans breaking the lines apart
                plt.scatter(spans, mi_diff_series, c="k")
                plt.scatter(spans, t_diff_series, c="k")
                plt.legend()
                plt.xlabel("span")  # speaks for both subplots without wasting space (same x axis)
                plt.ylabel("agree - disagree")
                plt.xlim(min(spans)-0.5, max(spans)+0.5)  # force the x-axis to show all spans even if some have nan

            plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/{}_span_trajectory.png".format(target.replace("/","|")))
            plt.gcf().clear()
            # plt.show()

            # TODO: make similar plots of the metrics and diffs by span for all syncretic and all non-syncretic
            # essentially the form-grouping changes in a "sliding" way
            # which form-grouping is used for the collocates depends on what the target is
            # e.g. if the target is 23ns suffix, then the collocates need to be stated as agree/disagree with that
            # but then once you've moved on to a different suffix, the agree/disagree values should be changed
            # this way, can calculate aggregate agree/disagree association strengths for all syncretic at once
            # alternatively/additionally, can collect raw occurrence numbers 
            # - (the counts that go into the calculation of the metrics) 
            # - and just return those instead of the whole metric, 
            # - and then calculate the metric for the whole set of syncretic suffixes 
            # - by aggregating those numbers somehow

    # now out of for loop that goes over each affix, have trajectories for all morphemes    
    # make big plot of all suffix trajectories, color code by syncretism
    if make_plots:
        if not restrict_to_agree:
            raise Exception("don't plot disagree for the all-suffix trajectories")
        for target, trajectory_dict in trajectories.items():
            # MI plot
            plt.subplot(2,1,1)
            mi_agree_series = trajectory_dict["mi_agree"]
            line_color = "r" if trajectory_dict["is_syncretic"] else "k"
            plt.plot(spans, mi_agree_series, c=line_color, alpha=0.5)
            # if not restrict_to_agree:
            #     mi_disagree_series = trajectory_dict["mi_disagree"]
            #     plt.plot(spans, mi_disagree_series, c="r", alpha=0.5)
            # also do scatter points since lines won't show up if there are nans next to a point
            plt.scatter(spans, mi_agree_series, c="k", alpha=0.5)
            # if not restrict_to_agree:
            #     plt.scatter(spans, mi_disagree_series, c=point_color, alpha=0.5)
            # make manual legend, from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
            # rather than labeling each series individually
            patch1 = mpatches.Patch(color="r", label="syncretic")
            patch2 = mpatches.Patch(color="k", label="non-syncretic")
            legend_handles = [patch1, patch2]
            # if not restrict_to_agree:
            #     legend_handles += [mi_disagree_patch]
            plt.legend(handles=legend_handles)
            plt.title("all_trajectories")
            plt.ylabel("MI")
            plt.xlim(min(spans)-0.5, max(spans)+0.5)  # force the x-axis to show all spans even if some have nan

            # T plot
            plt.subplot(2,1,2)
            t_agree_series = trajectory_dict["t_agree"]
            line_color = "r" if trajectory_dict["is_syncretic"] else "k"
            plt.plot(spans, t_agree_series, c=line_color, alpha=0.5)
            # if not restrict_to_agree:
            #     t_disagree_series = trajectory_dict["t_disagree"]
            #     plt.plot(spans, t_disagree_series, c="m", alpha=0.5)
            # also do scatter points since lines won't show up if there are nans next to a point
            plt.scatter(spans, t_agree_series, c="k", alpha=0.5)
            # if not restrict_to_agree:
            #     plt.scatter(spans, t_disagree_series, c=point_color, alpha=0.5)
            # make manual legend, from https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
            # rather than labeling each series individually
            patch1 = mpatches.Patch(color="r", label="syncretic")
            patch2 = mpatches.Patch(color="k", label="non-syncretic")
            legend_handles = [patch1, patch2]
            # if not restrict_to_agree:
            #     t_disagree_patch = mpatches.Patch(color="m", label="T disagree")
            #     legend_handles += [t_disagree_patch]
            plt.legend(handles=legend_handles)
            # don't plt.title this one
            plt.ylabel("T")
            plt.xlim(min(spans)-0.5, max(spans)+0.5)  # force the x-axis to show all spans even if some have nan
            plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/all_trajectory.png")
            # don't clear the figure


def report_regression_results(target_affix_morpheme_collection, offset_positions):
    # fit regression: Offset ~ IsSyncreticForPerson + IsSyncreticForNumber + error
    # https://realpython.com/linear-regression-in-python/#implementing-linear-regression-in-python
    ys = []
    xs = []
    for target_affix_morpheme in target_affix_morpheme_collection.get_morphemes():
        morph = target_affix_morpheme.morph
        is_syncretic_for_person = target_affix_morpheme.is_syncretic_for_person()
        is_syncretic_for_number = target_affix_morpheme.is_syncretic_for_number()
        # offset dictionary is keyed on morph, then gives dict from offset position to list of pronouns with that offset
        offsets = offset_positions[morph]
        for offset_amount, pronoun_token_lst in offsets.items():
            assert type(offset_amount) is int
            assert type(pronoun_token_lst) is list
            for pronoun_token in pronoun_token_lst:
                # count each as a separate data point in the regression
                ys.append(offset_amount)
                x_person = int(is_syncretic_for_person)  # int(bool) -> 0, 1
                x_number = int(is_syncretic_for_number)
                x = [x_person, x_number]
                xs.append(x)
    # now fit the regression
    print("\n-- fitting linear regression for offset amount")
    xs = np.array(xs)
    ys = np.array(ys)
    # sklearn doesn't have nice summary
    # model = LinearRegression().fit(xs, ys)
    # r_sq = model.score(xs, ys)
    # print("R Squared:", r_sq)
    # print("intercept:", model.intercept_)
    # print("slope:", model.coef_)
    xs = sm.add_constant(xs)  # needed for intercept fitting, see https://stackoverflow.com/questions/20701484/why-do-i-get-only-one-parameter-from-a-statsmodels-ols-fit
    regression_summary1 = sm.OLS(ys, xs).fit().summary()
    print(regression_summary1)

    # second regression: abs of offset, i.e., closeness to verb
    print("\n-- fitting linear regression for abs of offset amount")
    ys2 = abs(ys)
    regression_summary2 = sm.OLS(ys2, xs).fit().summary()
    print(regression_summary2)

    print("average offset = {}".format(np.mean(ys)))  # check if the intercept is too messed up by bad slopes


def plot_distribution_of_sentence_lengths(sentences):
    # wordforms only, no punctuation
    min_len = 1000000  # hacky
    max_len = -1000000
    counts = {}
    for sentence in sentences:
        x = len([w for w in sentence if type(w) is WordForm])
        if x not in counts:
            counts[x] = 0
        counts[x] += 1
        if x < min_len:
            min_len = x
        if x > max_len:
            max_len = x
    width = 0.5
    xs = list(range(min_len, max_len+1))
    counts_series = [counts.get(x, 0) for x in xs]
    plt.bar(xs, counts_series, width, color="blue")
    plt.title("sentence length (words) without punctuation")
    plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/sentence_lengths.png")


def get_form_group_agree_disagree_with_affix(wf, affix, restrict_to_agree):
    assert type(wf) is WordForm
    assert type(affix) is TargetAffixMorpheme
    affix_morph = affix.morph
    affix_agreement_info = get_agreement_info_from_morph(affix_morph)
    if wf.contains_pos(PRONOUN_POS_STR):
        pronoun_morphemes = wf.get_morphemes_by_pos(PRONOUN_POS_STR, gloss_regex=PRONOUN_GLOSS_REGEX, max_results=1)
        if len(pronoun_morphemes) == 0:
            # spurious, treat it like a non-pronoun word, just collocate based on the text form
            return wf.text
        wf_agreement_info = get_agreement_info_from_morph(pronoun_morphemes[0])
        if agreement_infos_agree(wf_agreement_info, affix_agreement_info):
            return AGREE_STR
        elif restrict_to_agree:
            # don't group others into "disagree", just return the word
            return wf.text
        else:
            # not restricting to agree only, so group other pronouns as "disagree"
            return DISAGREE_STR
    else:
        return wf.text


def get_agreement_info_from_morph(morph):
    return morph.gloss.split(".")[0]  # true of suffixes AND pronouns, in Don Daniels glossing convention


def pronoun_and_suffix_agree(pronoun_morph, suffix_morph):
    return agreement_infos_agree(get_agreement_info_from_morph(pronoun_morph), get_agreement_info_from_morph(suffix_morph))


def agreement_infos_agree(g1, g2):
    return persons_agree(get_person(g1), get_person(g2)) and numbers_agree(get_number(g1), get_number(g2))


def persons_agree(x123, y123):
    return len(set(int(x) for x in x123) & set(int(x) for x in y123)) > 0  # implicit type checking for str composed of int chars


def numbers_agree(xsdp, ysdp):
    number_agreements = {"s": ["s"], "ns": ["d","p","ns"], "d":["d","ns"], "p":["p","ns"]}
    return ysdp in number_agreements[xsdp]


def get_person(g):
    return "".join(x for x in g if x in "123")  # confusingly, person is referred to by number chars


def get_number(g):
    return "".join(x for x in g if x in "nsdp")  # get rid of clusivity for now


def get_suffix_finality(suffix_morph):
    # specific to Bongu language
    # returns "medial" or "final" for valid suffixes, specific to Don Daniels glossing conventions
    gloss = suffix_morph.gloss
    gloss_components = gloss.split(".")
    medial_tags = ["ss", "ds"]
    final_tags = ["fpst", "rpst", "prs", "ifut", "fut", "imp", "irr"]
    if any(component in medial_tags for component in gloss_components):
        # check these first, they will override the others, e.g. irr.ds is medial, not final
        return "medial"
    elif any(component in final_tags for component in gloss_components):
        return "final"
    else:
        raise Exception("gloss unclassifiable for finality: {}".format(gloss))



if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    include_punctuation = True
    corpus = Corpus(project_dir, project_name, include_punctuation)

    texts_to_include = None  # pass as None to get all non-omitted texts
    # texts_to_include = ["Help"]  # test stuff with a single shorter text
    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    wordform_contents = corpus.get_wordform_contents(
        texts_separated=True,
        sentences_separated=True,
        paragraphs_separated=False,
        texts_to_include=texts_to_include,
        texts_to_omit=texts_to_omit,
    )
    # print(wordform_contents)
    sentences = []
    for text in wordform_contents:
        for sentence in text:
            sentences.append(sentence)
    # now we have each sentence as a separate item in a list, no longer arranged hierarchically by text
    plot_distribution_of_sentence_lengths(sentences)
    
    verbose = True

    syncretic_affixes, non_syncretic_affixes = get_syncretic_and_non_syncretic_affixes(
        bongu_agreement_affixes, verbose=verbose,
    )

    # now go through the whole corpus, get any morphemes that match something in the affix list
    final_morphemes = get_all_final_morphemes_in_corpus(sentences, verbose=verbose)
    if verbose:
        print("\n-- finding affixes matching each word-final morpheme")
    target_affix_morpheme_collection = get_target_affix_morpheme_collection(
        final_morphemes, bongu_agreement_affixes, verbose=verbose,
    )

    # now that we have the affixes we're interested in, for each of them, find where the pronouns occur
    offset_positions = get_nearest_pronoun_offset_positions(
        target_affix_morpheme_collection, sentences, restrict_to_agree=True,
    )

    # finished, look at the resulting offset positions and morphemes
    print("offset positions:", offset_positions)
    # digest the info more easily, look just at the glosses of the morphs
    agree_disagree_counts = get_agree_disagree_counts(
        target_affix_morpheme_collection, offset_positions, verbose=verbose,
    )
    plot_agree_disagree_counts_by_morpheme(
        target_affix_morpheme_collection, agree_disagree_counts,
    )
    plot_agree_disagree_counts_by_syncretism(
        target_affix_morpheme_collection, agree_disagree_counts,
    )

    print("\n-- reporting affix collocations")
    report_affix_collocations(
        target_affix_morpheme_collection, sentences, make_plots=True,
        restrict_to_agree=True,
    )
    # measure difference in collocation with agreeing/disagreeing for each suffix, over a variety of spans
    # graph the change in this more-agreeing-pronouns metric as you change span

    # see if pronoun location offset can be predicted from syncretism
    report_regression_results(target_affix_morpheme_collection, offset_positions)
