import re

# from flexpy.Morpheme import Morpheme
from flexpy.TagDict import TagDict
# from flexpy.WordAnalysis import WordAnalysis
from flexpy.FlexPyUtil import (
    get_strs_from_form, get_single_str_from_form, get_unique_strs_from_form_as_list,
)

from flexpy.tags.RtLexEntry import RtLexEntry
from flexpy.tags.RtWfiAnalysis import RtWfiAnalysis
from flexpy.tags.RtWfiMorphBundle import RtWfiMorphBundle
from flexpy.tags.RtWfiWordform import RtWfiWordform


class WordForm:
    """Contains the information about a single word, which may be from a text, 
        or an item in the lexicon.

    :param forms: the list of forms for each morpheme
    :type forms: list<str>
    :param citation_forms: the list of citation forms for each morpheme
    :type citation_forms: list<str>
    :param morph_types: the list of morph types for each morpheme
    :type morph_types: list<str>
    :param glosses: the list of glosses for each morpheme
    :type glosses: list<str>
    :param poses: the list of parts of speech for each morpheme
    :type poses: list<str>
    :param tag_dict:
    :type tag_dict: TagDict
    """
    def __init__(self, baseline, forms, citation_forms, morph_types, glosses, poses, lex_entry_guids, tag_dict):
        assert type(tag_dict) is TagDict, type(tag_dict)
        self.tag_dict = tag_dict
        self.baseline = baseline
        self.morpheme_forms = forms
        self.citation_forms = citation_forms
        self.morph_types = morph_types
        self.glosses = glosses
        self.poses = poses
        self.lex_entry_guids = lex_entry_guids
        self.morphemes = self.get_morphemes()

    def __repr__(self):
        return f"<WordForm \"{self.baseline}\" {self.morpheme_forms} ({self.morph_types}) = ({self.poses}) {self.glosses}>"

    # for baseline, don't just join all the morpheme forms, e.g. some things might remain unparsed, or the morpheme form is zero, or some other such thing
    # - need to get the actual baseline string that exists regardless of the word analysis
    # TP1 22, first word is "hameme" (after beginning parenthesis)
    # - rt StTxtPara > Segments > only one objsur > rt Segment > Analyses > second objsur (9ee17149-0f0e-4f05-a0e1-d24f61adb0ba)
    # - rt WfiAnalysis with this ownerguid (this is not what we want, we want the rt with this guid itself)
    # - rt WfiWordform with this guid > Form > AUni = "hameme"
    # - but that could be the morpheme string rather than the word string
    # another: TP1 2, "ahe" after "mbuma", in baseline it has no acute, in morpheme it does, so we want to get "ahe" with no acute here
    # - rt StTxtPara > Segments > only one objsur > rt Segment > Analyses > seventh objsur (89e7660d-9a9b-4b51-8b13-a810805b415c)
    # - rt WfiWordform with this guid > Form > AUni = "ahe", so this is the correct path to find baseline string
    # - so rt WfiAnalysis has the MorphBundles and Meanings and other stuff associated with assigning an analysis to the wordform string itself
    # - and the owner of the rt WfiAnalysis is the rt WfiWordform that contains the actual baseline wordform string

    @staticmethod
    def from_rt_wfi_analysis(rt_wfi_analysis, tag_dict):
        assert type(rt_wfi_analysis) is RtWfiAnalysis, type(rt_wfi_analysis)
        owner = rt_wfi_analysis.get_owner()
        assert type(owner) is RtWfiWordform, type(owner)
        baseline = get_single_str_from_form(owner.Form())
        morph_bundles = rt_wfi_analysis.MorphBundles().RtWfiMorphBundle()
        forms = WordForm.create_forms(morph_bundles)
        citation_forms = WordForm.create_citation_forms(morph_bundles)
        morph_types = WordForm.create_morph_types(morph_bundles)
        glosses = WordForm.create_glosses(morph_bundles)
        poses = WordForm.create_poses(morph_bundles)
        lex_entry_guids = WordForm.create_lex_entry_guids(morph_bundles)
        return WordForm(baseline, forms, citation_forms, morph_types, glosses, poses, lex_entry_guids, tag_dict)

    @staticmethod
    def from_rt_wfi_gloss(rt_wfi_gloss, tag_dict):
        form_obj = rt_wfi_gloss.Form()
        # print(f"{form_obj = }")
        gloss = get_single_str_from_form(form_obj)
        glosses = [gloss]

        gloss_owner = rt_wfi_gloss.get_owner()
        if type(gloss_owner) is RtWfiMorphBundle:
            raise Exception("owner is a morph bundle")
            # unknown stuff from WfiGloss, get it from owner object
            rt_wfi_morph_bundle = gloss_owner
            form = WordForm.get_form_from_morph_bundle(rt_wfi_morph_bundle)
            forms = [form]
            citation_form = WordForm.get_citation_form_from_morph_bundle(rt_wfi_morph_bundle)
            citation_forms = [citation_form]
            morph_type = WordForm.get_morph_type_from_morph_bundle(rt_wfi_morph_bundle)
            morph_types = [morph_type]
            pos = WordForm.get_pos_name_from_morph_bundle(rt_wfi_morph_bundle)
            poses = [pos]
            lex_entry_guids = WordForm.get_lex_entry_guid_from_morph_bundle(rt_wfi_morph_bundle)
            return WordForm(baseline, forms, citation_forms, morph_types, glosses, poses, lex_entry_guids, tag_dict)
        elif type(gloss_owner) is RtWfiAnalysis:
            wordform_from_wfi_analysis = WordForm.from_rt_wfi_analysis(gloss_owner, tag_dict)

            # used to overwrite the gloss, but now want to make sure we get gloss for each morpheme, so don't do this
            # wordform_from_wfi_analysis.glosses = glosses  # overwrite with the more accurate gloss we already know
            return wordform_from_wfi_analysis
        else:
            raise TypeError("can't handle gloss owner: {}".format(gloss_owner))
    
    @staticmethod
    def from_rt_wfi_wordform(rt_wfi_wordform, tag_dict):
        # if we're here, it's because we just need the form and can't get anything else
        # the WfiWordform may indeed have some Analyses (if it is a wordform known in the Word Analyses tab)
        # - but here we don't know which analysis it should have, so don't get any parse data
        baseline = get_single_str_from_form(rt_wfi_wordform.Form())
        forms = [baseline]
        citation_forms = [None]
        morph_types = [None]
        glosses = [None]
        poses = [None]
        lex_entry_guids = [None]
        return WordForm(baseline, forms, citation_forms, morph_types, glosses, poses, lex_entry_guids, tag_dict)

    # def create_analyses(self):
    #     # one WordAnalysis object for each separate analysis of the word (i.e. different glosses of the morphemes)
    #     # this will correspond to one analysis for each morph bundle
    #     rt_wfi_analyses = self.rt_wfi_wordform.Analyses.RtWfiAnalysis
    #     word_analyses = []
    #     for rt_wfi_analysis in rt_wfi_analyses:
    #         rt_wfi_morph_bundles = rt_wfi_analysis.MorphBundles.RtWfiMorphBundle
    #         word_analysis = WordAnalysis.from_rt_wfi_morph_bundles(rt_wfi_morph_bundles)
    #         word_analyses.append(word_analysis)
    #     # print("got word analyses:", word_analyses)
    #     return word_analyses
    
    @staticmethod
    def create_forms(morph_bundles):
        # don't create too many python objects where they're not needed
        forms = []
        for morph_bundle in morph_bundles:
            form = WordForm.get_form_from_morph_bundle(morph_bundle)
            if form is None:
                # print(f"got form None from {morph_bundle = }")
                form = ""
            forms.append(form)
        return forms
    
    @staticmethod
    def create_citation_forms(morph_bundles):
        citation_forms = []
        for morph_bundle in morph_bundles:
            citation_form = WordForm.get_citation_form_from_morph_bundle(morph_bundle)
            citation_forms.append(citation_form)
        return citation_forms

    @staticmethod
    def create_morph_types(morph_bundles):
        morph_types = []
        for morph_bundle in morph_bundles:
            morph_type = WordForm.get_morph_type_from_morph_bundle(morph_bundle)
            morph_types.append(morph_type)
        return morph_types
    
    @staticmethod
    def create_glosses(morph_bundles):
        glosses = []
        for morph_bundle in morph_bundles:
            gloss = WordForm.get_gloss_from_morph_bundle(morph_bundle)
            glosses.append(gloss)
        return glosses

    @staticmethod
    def create_poses(morph_bundles):
        poses = []
        for morph_bundle in morph_bundles:
            pos = WordForm.get_pos_name_from_morph_bundle(morph_bundle)
            poses.append(pos)
        return poses

    @staticmethod
    def create_lex_entry_guids(morph_bundles):
        guids = []
        for morph_bundle in morph_bundles:
            guid = WordForm.get_lex_entry_guid_from_morph_bundle(morph_bundle)
            guids.append(guid)
        return guids

    @staticmethod
    def get_form_from_morph_bundle(morph_bundle):
        form = morph_bundle.Form()
        if form is None:
            return None
        return get_single_str_from_form(form)

    @staticmethod
    def get_allomorph_form_from_morph_bundle(morph_bundle):
        morph = morph_bundle.Morph()
        if morph is None:
            return None
        stem_allomorph = morph.RtMoStemAllomorph()
        affix_allomorph = morph.RtMoAffixAllomorph()
        if len(stem_allomorph) > 0:
            assert affix_allomorph == [], "Morph bundle with stem and affix forms: {} -> {} + {}".format(morph_bundle, stem_allomorph, affix_allomorph)
            assert len(stem_allomorph) == 1, stem_allomorph
            allomorph = stem_allomorph[0]
        elif len(affix_allomorph) > 0:
            assert stem_allomorph == [], "Morph bundle with stem and affix forms: {} -> {} + {}".format(morph_bundle, stem_allomorph, affix_allomorph)
            assert len(affix_allomorph) == 1, affix_allomorph
            allomorph = affix_allomorph[0]
        else:
            raise Exception("morph has neither stem nor affix allomorphs: {}".format(morph))
        return allomorph

    @staticmethod
    def get_citation_form_from_morph_bundle(morph_bundle):
        # affix allomorphy organization in FLEx XML
        # RtMoAffixAllomorph (e.g. -yesen, allomorph of -esen) has ownerguid for RtLexEntry
        # RtLexEntry has LexemeForm, objsur to RtMoAffixAllomorph
        # e.g. RtMoAffixAllomorph -esen (citation form) ea365d7a-a0bc-450e-b9e5-e6c61804bcd9
        # - owned by RtLexEntry a89632fa-140c-409d-9b33-26dddcc8a4db
        # RtLexEntry also has AlternateForms, objsur to RtMoAffixAllomorph
        # e.g. the LexEntry for -esen has AlternateForms 4e896046-03f7-4e6f-9ba3-c1dc96f0d5b2
        # - this is the RtMoAffixAllomorph for -yesen
        # RtWfiMorphBundle has child Morph, objsur to RtMoStemAllomorph, owned by RtLexEntry

        allomorph = WordForm.get_allomorph_form_from_morph_bundle(morph_bundle)
        if allomorph is None:
            return None
        owner = allomorph.get_owner()
        assert type(owner) is RtLexEntry, owner
        lex_entry = owner
        lex_form = lex_entry.LexemeForm()
        # now we have the object containing the citation allomorph of this morpheme
        # there are only two allomorph types, RtMoStemAllomorph and RtMoAffixAllomorph
        stem_allomorph = lex_form.RtMoStemAllomorph()
        affix_allomorph = lex_form.RtMoAffixAllomorph()
        if len(stem_allomorph) > 0:
            assert affix_allomorph == [], "LexEntry with stem and affix citation: {} -> {} + {}".format(lex_entry, stem_allomorph, affix_allomorph)
            assert len(stem_allomorph) == 1, stem_allomorph
            allomorph = stem_allomorph[0]
        elif len(affix_allomorph) > 0:
            assert stem_allomorph == [], "LexEntry with stem and affix citation: {} -> {} + {}".format(lex_entry, stem_allomorph, affix_allomorph)
            assert len(affix_allomorph) == 1, affix_allomorph
            allomorph = affix_allomorph[0]
        else:
            raise Exception("LexEntry with neither stem nor affix citation: {}".format(lex_entry))

        # sometimes get LexEntry with multiple forms for some reason, store them as list
        forms = get_unique_strs_from_form_as_list(allomorph.Form())
        if len(forms) == 1:
            return forms[0]
        else:
            print("warning: LexEntry found with {} forms: {}".format(len(forms), forms))
            assert all("," not in x for x in forms), "forms contain commas: {}".format(forms)
            return forms
        # citation_form_str = get_single_str_from_form(allomorph.Form(), allow_repeat=True)
        # return citation_form_str
    
    @staticmethod
    def get_morph_type_from_morph_bundle(morph_bundle):
        morph_types = []
        morph = morph_bundle.Morph()
        if morph is None:
            return None
        rt_mo_affix_allomorph = morph.RtMoAffixAllomorph()
        rt_mo_stem_allomorph = morph.RtMoStemAllomorph()
        # print("Morph stuff:", rt_mo_affix_allomorph, rt_mo_stem_allomorph)
        for allomorph_lst in [rt_mo_affix_allomorph, rt_mo_stem_allomorph]:
            for allomorph in allomorph_lst:
                # print("stuff in allomorph {}".format(allomorph))
                form = allomorph.Form()
                strs = get_strs_from_form(form)
                # print("form strs: {}".format(strs))
                morph_type = allomorph.MorphType()
                rt_mo_morph_types = morph_type.RtMoMorphType()
                for rt_mo_morph_type in rt_mo_morph_types:
                    name_aunis = rt_mo_morph_type.Name().AUni()
                    eng_aunis = [x for x in name_aunis if x.ws == "en"]
                    assert len(eng_aunis) == 1, eng_aunis
                    morph_type_name = eng_aunis[0].text
                    # print("morph type name: {}".format(morph_type_name))
                    morph_types.append(morph_type_name)
        assert len(morph_types) == 1, morph_types
        return morph_types[0]
    
    @staticmethod
    def get_pos_name_from_morph_bundle(morph_bundle):
        pos_names = []
        msa = morph_bundle.Msa()
        if msa is None:
            return None
        rt_mo_deriv_aff_msa = msa.RtMoDerivAffMsa()
        rt_mo_infl_aff_msa = msa.RtMoInflAffMsa()
        rt_mo_stem_msa = msa.RtMoStemMsa()
        rt_mo_unclassified_affix_msa = msa.RtMoUnclassifiedAffixMsa()
        # print("Msa stuff:", rt_mo_deriv_aff_msa, rt_mo_infl_aff_msa, rt_mo_stem_msa, rt_mo_unclassified_affix_msa)
        for sub_msa_lst in [rt_mo_deriv_aff_msa, rt_mo_infl_aff_msa, rt_mo_stem_msa, rt_mo_unclassified_affix_msa]:
            # print("parts of speech in {}".format(sub_msa_lst))
            for sub_msa in sub_msa_lst:
                if sub_msa.__class__.__name__ == "RtMoDerivAffMsa":
                    from_pos = sub_msa.FromPartOfSpeech()
                    to_pos = sub_msa.ToPartOfSpeech()
                    poses = [from_pos, to_pos]
                else:
                    pos = sub_msa.PartOfSpeech()
                    if pos is None:
                        pos_names.append(None)
                        continue
                    poses = [pos]
                these_pos_names = []
                for pos in poses:
                    if pos is None:
                        continue
                    for rt_pos in pos.RtPartOfSpeech():
                        catalog_source_id = rt_pos.CatalogSourceId()  # where the full pos name is stored
                        if catalog_source_id is not None:
                            pos_name = catalog_source_id.Uni().text
                            these_pos_names.append(pos_name)
                this_pos_name = ">".join(these_pos_names)  # for DerivationalAffix, e.g. Noun>Verb
                pos_names.append(this_pos_name)
        assert len(pos_names) == 1, pos_names
        return pos_names[0]
    
    @staticmethod
    def get_lex_entry_guid_from_morph_bundle(morph_bundle):
        allomorph = WordForm.get_allomorph_form_from_morph_bundle(morph_bundle)
        if allomorph is None:
            return None
        lex_entry = allomorph.get_owner()
        assert type(lex_entry) is RtLexEntry, lex_entry
        return lex_entry.guid

    @staticmethod
    def get_gloss_from_morph_bundle(morph_bundle):
        glosses = []
        sense = morph_bundle.Sense()
        if sense is None:
            return None
        rt_lex_senses = sense.RtLexSense()
        for rt_lex_sense in rt_lex_senses:
            gloss = rt_lex_sense.Gloss()
            if gloss is None:
                continue
            aunis = gloss.AUni()
            for auni in aunis:
                gloss_text = auni.text
                glosses.append(gloss_text)
        if len(glosses) == 0:
            return None
        assert len(glosses) == 1, glosses
        return glosses[0]

    def get_root_pos(self):
        root_indices = [i for i, x in enumerate(self.morph_types) if x == "root"]
        root_poses = [self.poses[i] for i in root_indices]
        unique_root_poses = list(set(root_poses))
        if len(unique_root_poses) == 0:
            return None
        elif len(unique_root_poses) > 1:
            raise Exception("word with more than one root part of speech: {}".format(self))
        return unique_root_poses[0]

    def get_morphemes(self):
        res = []
        for form, citation_form, morph_type, gloss, pos, lex_entry_guid in zip(
            self.morpheme_forms, self.citation_forms, self.morph_types, self.glosses, self.poses, self.lex_entry_guids,
        ):
            morph = WordFormMorpheme(form, citation_form, morph_type, gloss, pos, lex_entry_guid, self.tag_dict)
            res.append(morph)
        return res
    
    def contains_pos(self, pos):
        return any(morph.pos == pos for morph in self.morphemes)

    def get_morphemes_by_pos(self, pos, gloss_regex=None, max_results=None):
        morphemes_of_pos = [m for m in self.morphemes if m.pos == pos]
        if gloss_regex is not None:
            morphemes_of_pos = [m for m in morphemes_of_pos if re.match(gloss_regex, m.gloss)]
        if max_results is not None:
            if len(morphemes_of_pos) > max_results:
                raise Exception("got too many results for pos {} and regex {}: {}".format(pos, gloss_regex))
        return morphemes_of_pos

    def get_subgloss_by_pos(self, pos):
        # returns only the components of the gloss that are from morphemes with this part of speech
        morphemes_of_pos = [m for m in self.morphemes if m.pos == pos]
        return "-".join(m.gloss for m in morphemes_of_pos)

    def __eq__(self, other):
        if type(other) is not WordForm:
            return NotImplemented
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))


class WordFormMorpheme:
    """Contains information about a single morpheme within a WordForm.

    :param form:
    :type form: str
    :param citation_form:
    :type citation_form: str
    :param morph_type:
    :type morph_type: str
    :param gloss:
    :type gloss: str
    :param pos: part of speech
    :type pos: str
    :param tag_dict:
    :type tag_dict: TagDict
    """
    def __init__(self, form, citation_form, morph_type, gloss, pos, lex_entry_guid, tag_dict):
        assert type(tag_dict) is TagDict, type(tag_dict)
        self.tag_dict = tag_dict
        self.form = form
        self.citation_form = citation_form
        self.morph_type = morph_type
        self.gloss = gloss
        self.pos = pos
        self.lex_entry_guid = lex_entry_guid

    def __repr__(self):
        # since __eq__ and __hash__ depend on __repr__, use citation form so allomorphs are treated as equal
        # removed pos from this for now since the inconsistency of labeling of affix POSes created multiple different morpheme objects that were really the same morpheme
        return "<WordFormMorpheme \"{}\" ({}) = \"{}\">".format(self.citation_form, self.morph_type, self.gloss)

    def __eq__(self, other):
        if type(other) is not WordFormMorpheme:
            return NotImplemented
        return repr(self) == repr(other)
    
    def __hash__(self):
        return hash(repr(self))
