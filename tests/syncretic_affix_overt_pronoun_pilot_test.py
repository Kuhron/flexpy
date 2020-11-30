import math
import re
import matplotlib.pyplot as plt
import numpy as np

# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.Corpus import Corpus
from flexpy.CorpusAnalysis import collocator_separating_target_and_collocate_terms
from flexpy.Text import Text
from flexpy.WordForm import WordForm, WordFormMorpheme


def get_form_group_last_morpheme(wordform):
    morph = wordform.morphemes[-1]
    morph_type = morph.morph_type
    form = morph.form
    if form is None:
        return "None"
    elif morph_type in [None, "None"]:
        return "None"
    elif morph_type in ["root", "stem", "particle", "phrase"]:
        form_notation = form
    elif morph_type == "bound root":
        form_notation = "*" + form
    elif morph_type == "suffix":
        form_notation = "-" + form
    elif morph_type == "prefix":
        form_notation = form + "-"
    elif morph_type == "enclitic":
        form_notation = "=" + form
    elif morph_type == "proclitic":
        form_notation = form + "="
    else:
        raise Exception("unknown morph type: {}, in wordform: {}".format(morph_type, wordform))
    gloss = wordform.glosses[-1]
    return "{} ({})".format(form_notation, gloss)


def get_form_group_last_morpheme_form(wordform):
    return wordform.forms[-1]


def get_form_group_last_morpheme_gloss(wordform):
    return wordform.glosses[-1]


def group_wordforms(tokenized, grouping_function):
    new_tokenized = []
    for text in tokenized:
        new_text = group_wordforms_in_text(text, grouping_function)
        new_tokenized.append(new_text)
    return new_tokenized


def group_wordforms_in_text(text, grouping_function):
    new_text = []
    for token in text:
        new_token = grouping_function(token)
        new_text.append(new_token)
    return new_text


def report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms):
    words_of_interest = ["aji", "ni", "andu"]
    metrics = ["MI", "T"]
    for word in words_of_interest:
        for metric in metrics:
            collocates = collocator_separating_target_and_collocate_terms(
                corpus_in_target_terms,
                corpus_in_collocate_terms,
                word, left=4, right=4, stat=metric, cutoff=5, ignore=[]
            )
            print("----\nCollocations for {} using stat={}:".format(word, metric))
            ct.head(collocates, hits=10)


if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    wordform_contents = corpus.get_wordform_contents(
        texts_separated=True,
        paragraphs_separated=False,
        texts_to_omit=texts_to_omit,
    )

    bongu_agreement_affixes_tuples = [
        ("aim", r"2s\.fpst"),
        ("ain", r"3s\.fpst"),
        ("am", r"2s\.ifut"),
        ("an", r"3s\.ifut"),
        # ("aq", r"irr.*"),  # could agree with anything, so can't distinguish agree from disagree
        ("balan", r"23ns.*"),
        ("ban", r"23ns.*"),
        ("beb", r"23ns.*"),
        ("beben", r"23ns.*"),
        ("ber", r"23ns.*"),
        ("beren", r"23ns.*"),
        ("berlan", r"23d.*"),
        ("bes", r"23ns.*"),
        ("besen", r"23ns.*"),
        ("beslan", r"23d.*"),
        ("buleren", r"23d.*"),
        # "-bun" is not well understood
        ("bus", r"3ns.*"),
        ("busen", r"3ns.*"),
        ("busun", r"3ns.*"),
        ("e", r"2s\.imp"),
        ("eben", r"23ns.*"),
        ("eblan", r"23d.*"),
        ("em", r"2s.*"),
        ("emen", r"1s\.fpst"),  # don't use character class like r"[12]" because then it will think it's syncretic for person (has substr "12")
        ("emen", r"2s\.fut\?"),  # just treat this as a separate suffix from -emen 1s.fpst
        ("emun", r"1ns.*"),
        ("en", r"3s.*"),
        ("eqen", r"3s\.prs\?"),
        ("eren", r"3s.*"),
        ("es", r"3s\.r\.ss"),  # this one is not syncretic
        # ("es", r"irr.*"),  # this one IS syncretic, for all person and numbers  # can't distinguish agreeing from disagreeing pronouns
        ("esen", r"3s.*"),
        # -esen as different-subject marker is not well understood
        ("ib", r"2ns\.imp"),
        # -im not understood
        ("man", r"1s.*"),
        ("mem", r"1s.*"),
        ("memen", r"1s.*"),
        ("memes", r"12s.*"),
        ("meq", r"2s.*"),
        ("meqen", r"2s.*"),
        ("mere", r"2s.*"),
        ("meren", r"12s.*"),
        ("mes", r"12s.*"),
        ("mesen", r"12s.*"),
        ("mulan", r"1d\.rpst"),
        ("mum", r"1ns.*"),
        ("mun", r"1ns.*"),
        ("mur", r"1ns.*"),
        ("muren", r"1ns.*"),
        ("mus", r"1ns.*"),
        ("musen", r"1ns.*"),
    ]

    has_person_feature = lambda tup: any(x in tup[1] for x in ["1", "2", "3"])
    is_syncretic_for_person = lambda tup: any(x in tup[1] for x in ["12", "23"]) or not has_person_feature(tup)
    is_syncretic_for_number = lambda tup: "ns" in tup[1] or not has_person_feature(tup)  # e.g. irr.ss has no person or number feature, is syncretic to the max
    is_syncretic = lambda tup: is_syncretic_for_person(tup) or is_syncretic_for_number(tup)

    syncretic_affixes_for_person_tuples = [tup for tup in bongu_agreement_affixes_tuples if is_syncretic_for_person(tup)]
    syncretic_affixes_for_number_tuples = [tup for tup in bongu_agreement_affixes_tuples if is_syncretic_for_number(tup)]
    syncretic_affixes = [tup for tup in bongu_agreement_affixes_tuples if is_syncretic(tup)]
    non_syncretic_affixes = [tup for tup in bongu_agreement_affixes_tuples if not is_syncretic(tup)]

    print("\n-- syncretic affixes:")
    for x in syncretic_affixes:
        print(x)
    print("\n-- non-syncretic affixes:")
    for x in non_syncretic_affixes:
        print(x)

    # now go through the whole corpus, get any morphemes that match something in the affix list
    all_wordforms = set()
    for text in wordform_contents:
        for wf in text:
            all_wordforms.add(wf)
    final_morphemes = set()
    for wf in all_wordforms:
        # final_morpheme = get_form_group_last_morpheme(wf)
        final_morpheme = wf.morphemes[-1]
        final_morphemes.add(final_morpheme)
    # print("\n-- all word-final morphemes in corpus")
    final_morphemes = sorted(final_morphemes, key=repr)
    for x in final_morphemes:
        pass # print(x)
    # TODO need to be able to handle allomorphy! need to get the citation form of each morph when constructing WordForm, add self.citation_forms in addition to self.forms

    affix_matches_morpheme = lambda tup, morph: tup[0] == morph.form and morph.gloss is not None and re.match(tup[1], morph.gloss)
    affixes_matching_morpheme = lambda morph: [tup for tup in bongu_agreement_affixes_tuples if affix_matches_morpheme(tup, morph)]
    # print("\n-- finding affixes matching each word-final morpheme")
    target_affix_morphemes = {}
    for morph in final_morphemes:
        matches = affixes_matching_morpheme(morph)
        if len(matches) == 0:
            continue
        assert len(matches) == 1, "more than one match for morph {}: {}".format(morph, matches)
        # print(morph, matches)
        target_affix_morpheme_dict = {
            "morph": morph,
            "tup": matches[0],
            "is_syncretic_for_person": is_syncretic_for_person(matches[0]),
            "is_syncretic_for_number": is_syncretic_for_number(matches[0]),
            "is_syncretic": is_syncretic(matches[0]),
        }
        assert morph not in target_affix_morpheme_dict, "repeat morph {}".format(morph)
        target_affix_morphemes[morph] = target_affix_morpheme_dict
    print("\n-- all target affix morphemes:")
    for x in target_affix_morphemes:
        print(x)

    # now that we have the affixes we're interested in, for each of them, find where the pronouns occur
    wf_is_pronoun = lambda wf: any(morph.pos == "Pronoun" for morph in wf.morphemes)
    offset_positions = {}
    for target_affix_morpheme_dict in target_affix_morphemes.values():
        # for n in range(1, 11):
        #     left_span = n
        #     right_span = 1
        # get collocations, see what pronouns come up
        # restrict collocates to pronouns only if possible
        # I'm gonna do a custom thing here, get histogram of where the nearest pronoun is
        # get all tokens of this morpheme
        agreement_morpheme = target_affix_morpheme_dict["morph"]
        assert type(agreement_morpheme) is WordFormMorpheme
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
                        if wf_is_pronoun(left_wf):
                            pronoun_morphs = [m for m in left_wf.morphemes if m.pos == "Pronoun" and re.match(r"^[123].*", m.gloss)]  # don't include "pronouns" like "alone" or "emph"
                            if len(pronoun_morphs) == 0:
                                continue  # don't count this one, it was a spurious pronoun
                            elif len(pronoun_morphs) > 1:
                                raise Exception("got more than one pron in a wf: {}".format(left_wf))
                            pronoun_morph = pronoun_morphs[0]
                            offset_position = -1 * (left_j + 1)  # left_j=0 is first element left of target, thus offset is -1
                            if offset_position not in offset_positions[agreement_morpheme]:
                                offset_positions[agreement_morpheme][offset_position] = []
                            offset_positions[agreement_morpheme][offset_position].append(pronoun_morph)
                            break  # only do the nearest one
                    # simil nearest right
                    for right_j, right_wf in enumerate(right_context):
                        if wf_is_pronoun(right_wf):
                            pronoun_morphs = [m for m in right_wf.morphemes if m.pos == "Pronoun" and re.match(r"^[123].*", m.gloss)]  # don't include "pronouns" like "alone" or "emph"
                            if len(pronoun_morphs) == 0:
                                continue  # don't count this one, it was a spurious pronoun
                            elif len(pronoun_morphs) > 1:
                                raise Exception("got more than one pron in a wf: {}".format(right_wf))
                            pronoun_morph = pronoun_morphs[0]
                            offset_position = 1 + right_j  # right_j=0 is first element right, so offset is +1
                            if offset_position not in offset_positions[agreement_morpheme]:
                                offset_positions[agreement_morpheme][offset_position] = []
                            offset_positions[agreement_morpheme][offset_position].append(pronoun_morph)
                            break  # only do the nearest one
    
    # finished, look at the resulting offset positions and morphemes
    # print("offset positions:", offset_positions)
    # digest the info more easily, look just at the glosses of the morphs
    get_agreement_info_from_morph = lambda morph: morph.gloss.split(".")[0]  # true of suffixes AND pronouns
    pronoun_and_suffix_agree = lambda pronoun_morph, suffix_morph: agreement_infos_agree(get_agreement_info_from_morph(pronoun_morph), get_agreement_info_from_morph(suffix_morph))
    agreement_infos_agree = lambda g1, g2: persons_agree(get_person(g1), get_person(g2)) and numbers_agree(get_number(g1), get_number(g2))
    persons_agree = lambda x123, y123: len(set(int(x) for x in x123) & set(int(x) for x in y123)) > 0  # implicit type checking for str composed of int chars
    number_agreements = {"s": ["s"], "ns": ["d","p","ns"], "d":["d","ns"], "p":["p","ns"]}
    numbers_agree = lambda xsdp, ysdp: ysdp in number_agreements[xsdp]
    get_person = lambda g: "".join(x for x in g if x in "123")  # confusingly, person is referred to by number chars
    get_number = lambda g: "".join(x for x in g if x in "nsdp")  # get rid of clusivity for now
    agree_disagree_counts = {}
    for suffix_morph in target_affix_morphemes.keys():
        print("\n-- suffix morph: {}".format(target_affix_morphemes[suffix_morph]))
        suffix_gloss = suffix_morph.gloss
        agree_disagree_counts[suffix_morph] = {}
        for offset_position, pronouns in sorted(offset_positions[suffix_morph].items()):
            agree_count = 0
            disagree_count = 0
            pronoun_glosses = []
            for pronoun_morph in pronouns:
                agrees = pronoun_and_suffix_agree(pronoun_morph, suffix_morph)
                agree_str = "Agree" if agrees else "Disagree"
                pronoun_glosses.append("{} ({})".format(pronoun_morph.gloss, agree_str))
                if agrees:
                    agree_count += 1
                else:
                    disagree_count += 1
            agree_disagree_counts[suffix_morph][offset_position] = {0: disagree_count, 1: agree_count}
            print("offset {}: {}".format(offset_position, sorted(pronoun_glosses)))

        # plot stacked bar by offset
        min_offset = min(agree_disagree_counts[suffix_morph].keys())
        max_offset = max(agree_disagree_counts[suffix_morph].keys())
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

        # uncomment to re-make plots
        # p1 = plt.bar(xs, agree_counts, width, color="blue", label="agree {}".format(agree_num_text))
        # p2 = plt.bar(xs, disagree_counts, width, bottom=agree_counts, color="red", label="disagree {}".format(disagree_num_text))
        # plt.legend()
        # syncretism_bool = target_affix_morphemes[suffix_morph]["is_syncretic"]
        # plt.title("{} syncretic={}".format(suffix_gloss, syncretism_bool))
        # plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/{}_syncretic_{}.png".format(suffix_gloss.replace("/","|"), syncretism_bool))
        # plt.gcf().clear()
    
    # make stacked bar for all syncretic versus all non-syncretic
    for syncretism_bool in [True, False]:
        suffixes_of_this_syncretism = [suffix_morph for suffix_morph, d in target_affix_morphemes.items() if d["is_syncretic"] == syncretism_bool]
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

        # uncomment to re-make plots
        # p1 = plt.bar(xs, agree_counts, width, color="blue", label="agree {}".format(agree_num_text))
        # p2 = plt.bar(xs, disagree_counts, width, bottom=agree_counts, color="red", label="disagree {}".format(disagree_num_text))
        # plt.legend()
        # plt.title("all syncretic={}".format(syncretism_bool))
        # plt.savefig("/home/wesley/Desktop/UOregon Work/CorpusLinguistics/images/all_syncretism_{}.png".format(syncretism_bool))
        # plt.gcf().clear()


    # old, don't use this time
    # target_grouping_function = ?
    # collocate_grouping_function = get_form_group_last_morpheme
    # corpus_in_target_terms = group_wordforms(wordform_contents, target_grouping_function)
    # corpus_in_collocate_terms = group_wordforms(wordform_contents, grouping_function)
    # print("\n-- reporting pronoun collocations")
    # report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms)
