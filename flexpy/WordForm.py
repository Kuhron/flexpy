from flexpy.Morpheme import Morpheme
from flexpy.TagDict import TagDict
from flexpy.WordAnalysis import WordAnalysis

from flexpy.FlexPyUtil import get_strs_from_form

from flexpy.tags.RtWfiWordform import RtWfiWordform



class WordForm:
    def __init__(self, rt_wfi_wordform, tag_dict):
        assert type(rt_wfi_wordform) is RtWfiWordform, type(rt_wfi_wordform)
        assert type(tag_dict) is TagDict, type(tag_dict)
        self.rt_wfi_wordform = rt_wfi_wordform
        self.tag_dict = tag_dict
        # self.morph_bundles = self.create_morph_bundles()
        self.analyses = self.create_analyses()
        # self.forms = self.create_forms()
        # print("forms", self.forms)
        # self.morph_types = self.create_morph_types()
        # print("morph types", self.morph_types)
        # self.pos_names = self.create_pos_names()
        # print("pos", self.pos_names)
        # self.glosses = self.create_glosses()
        # print("glosses", self.glosses)
        # assert len(self.morph_bundles) == len(self.forms) == len(self.morph_types) == len(self.pos_names) == len(self.glosses)
        # input("\ndone with this WordForm, enter to continue\n")

    def create_analyses(self):
        # one WordAnalysis object for each separate analysis of the word (i.e. different glosses of the morphemes)
        # this will correspond to one analysis for each morph bundle

        rt_wfi_analyses = self.rt_wfi_wordform.Analyses.RtWfiAnalysis
        word_analyses = []
        for rt_wfi_analysis in rt_wfi_analyses:
            rt_wfi_morph_bundles = rt_wfi_analysis.MorphBundles.RtWfiMorphBundle
            word_analysis = WordAnalysis.from_rt_wfi_morph_bundles(rt_wfi_morph_bundles)
            word_analyses.append(word_analysis)
        return word_analyses

        # forms = self.create_forms()
        # morph_types = self.create_morph_types()
        # pos_names = self.create_pos_names()
        # glosses = self.create_glosses()
        # n = len(forms)
        # assert len(morph_types) == n
        # assert len(pos_names) == n
        # assert len(glosses) == n
        # for form, morph_type, pos_name, gloss in zip(forms, morph_types, pos_names, glosses):
        #     morpheme = Morpheme(form, morph_type, pos_name, gloss)
        #     print(morpheme)

    def create_forms(self):
        forms = []
        for morph_bundle in self.morph_bundles:
            form = morph_bundle.Form
            forms_dict = get_strs_from_form(form)
            has_astr = forms_dict["AStr"] is not None and forms_dict["AStr"] != []
            has_auni = forms_dict["AUni"] is not None and forms_dict["AUni"] != []
            has_str = forms_dict["Str"] is not None and forms_dict["Str"] != []
            assert has_astr + has_auni + has_str == 1, "forms_dict has != 1 valid forms: {}".format(forms_dict)
            for k, v in forms_dict.items():
                if v is not None:
                    assert type(v) is list, type(v)
                    if len(v) > 0:
                        # not empty list, there is some form here
                        assert len(v) == 1, "more than 1 form: {}".format(v)
                        forms.append(v)
        return forms

    def create_morph_types(self):
        morph_types = []
        for morph_bundle in self.morph_bundles:
            morph = morph_bundle.Morph
            if morph is None:
                morph_types.append(None)
                continue
            rt_mo_affix_allomorph = morph.RtMoAffixAllomorph
            rt_mo_stem_allomorph = morph.RtMoStemAllomorph
            # print("Morph stuff:", rt_mo_affix_allomorph, rt_mo_stem_allomorph)
            for allomorph_lst in [rt_mo_affix_allomorph, rt_mo_stem_allomorph]:
                for allomorph in allomorph_lst:
                    # print("stuff in allomorph {}".format(allomorph))
                    form = allomorph.Form
                    strs = get_strs_from_form(form)
                    # print("form strs: {}".format(strs))
                    morph_type = allomorph.MorphType
                    rt_mo_morph_types = morph_type.RtMoMorphType
                    for rt_mo_morph_type in rt_mo_morph_types:
                        name_aunis = rt_mo_morph_type.Name.AUni
                        eng_aunis = [x for x in name_aunis if x.ws == "en"]
                        assert len(eng_aunis) == 1, eng_aunis
                        morph_type_name = eng_aunis[0].text
                        # print("morph type name: {}".format(morph_type_name))
                        morph_types.append(morph_type_name)
        return morph_types

    def create_pos_names(self):
        pos_names = []
        for morph_bundle in self.morph_bundles:
            msa = morph_bundle.Msa
            if msa is None:
                pos_names.append(None)
                continue
            rt_mo_deriv_aff_msa = msa.RtMoDerivAffMsa
            rt_mo_infl_aff_msa = msa.RtMoInflAffMsa
            rt_mo_stem_msa = msa.RtMoStemMsa
            rt_mo_unclassified_affix_msa = msa.RtMoUnclassifiedAffixMsa
            # print("Msa stuff:", rt_mo_deriv_aff_msa, rt_mo_infl_aff_msa, rt_mo_stem_msa, rt_mo_unclassified_affix_msa)
            for sub_msa_lst in [rt_mo_deriv_aff_msa, rt_mo_infl_aff_msa, rt_mo_stem_msa, rt_mo_unclassified_affix_msa]:
                # print("parts of speech in {}".format(sub_msa_lst))
                for sub_msa in sub_msa_lst:
                    pos = sub_msa.PartOfSpeech
                    if pos is None:
                        pos_names.append(None)
                        continue
                    for rt_pos in pos.RtPartOfSpeech:
                        catalog_source_id = rt_pos.CatalogSourceId  # where the full pos name is stored
                        pos_name = catalog_source_id.Uni.text
                        pos_names.append(pos_name)
        return pos_names

    def create_glosses(self):
        glosses = []
        for morph_bundle in self.morph_bundles:
            sense = morph_bundle.Sense
            if sense is None:
                glosses.append(None)
                continue
            rt_lex_senses = sense.RtLexSense
            for rt_lex_sense in rt_lex_senses:
                gloss = rt_lex_sense.Gloss
                aunis = gloss.AUni
                for auni in aunis:
                    gloss_text = auni.text
                    glosses.append(gloss_text)
        return glosses
