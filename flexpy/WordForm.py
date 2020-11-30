# from flexpy.Morpheme import Morpheme
from flexpy.TagDict import TagDict
# from flexpy.WordAnalysis import WordAnalysis
from flexpy.FlexPyUtil import get_strs_from_form, get_single_str_from_form

from flexpy.tags.RtWfiAnalysis import RtWfiAnalysis
from flexpy.tags.RtWfiMorphBundle import RtWfiMorphBundle




class WordForm:
    def __init__(self, forms, morph_types, glosses, poses, tag_dict):
        assert type(tag_dict) is TagDict, type(tag_dict)
        self.tag_dict = tag_dict
        self.forms = forms
        self.morph_types = morph_types
        self.glosses = glosses
        self.poses = poses
        self.text = self.get_text()
        self.morphemes = self.get_morphemes()

    def __repr__(self):
        return "<WordForm \"{}\" ({}) = ({}) \"{}\">".format(self.forms, self.morph_types, self.poses, self.glosses)

    @staticmethod
    def from_rt_wfi_analysis(rt_wfi_analysis, tag_dict):
        assert type(rt_wfi_analysis) is RtWfiAnalysis, type(rt_wfi_analysis)
        morph_bundles = rt_wfi_analysis.MorphBundles().RtWfiMorphBundle()
        forms = WordForm.create_forms(morph_bundles)
        morph_types = WordForm.create_morph_types(morph_bundles)
        glosses = WordForm.create_glosses(morph_bundles)
        poses = WordForm.create_poses(morph_bundles)
        return WordForm(forms, morph_types, glosses, poses, tag_dict)

    @staticmethod
    def from_rt_wfi_gloss(rt_wfi_gloss, tag_dict):
        form_obj = rt_wfi_gloss.Form()
        if form_obj is None:
            return None
        gloss = get_single_str_from_form(form_obj)
        glosses = [gloss]

        gloss_owner = rt_wfi_gloss.get_owner()
        if type(gloss_owner) is RtWfiMorphBundle:
            # unknown stuff from WfiGloss, get it from owner object
            rt_wfi_morph_bundle = gloss_owner
            form = WordForm.get_form_from_morph_bundle(rt_wfi_morph_bundle)
            forms = [form]
            morph_type = WordForm.get_morph_type_from_morph_bundle(rt_wfi_morph_bundle)
            morph_types = [morph_type]
            pos = WordForm.get_pos_name_from_morph_bundle(rt_wfi_morph_bundle)
            poses = [pos]
            return WordForm(forms, morph_types, glosses, poses, tag_dict)
        elif type(gloss_owner) is RtWfiAnalysis:
            wordform_from_wfi_analysis = WordForm.from_rt_wfi_analysis(gloss_owner, tag_dict)

            # used to overwrite the gloss, but now want to make sure we get gloss for each morpheme, so don't do this
            # wordform_from_wfi_analysis.glosses = glosses  # overwrite with the more accurate gloss we already know
            return wordform_from_wfi_analysis
        else:
            raise TypeError("can't handle gloss owner: {}".format(rt_wfi_morph_bundle))        


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
            forms.append(form)
        return forms

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
    def get_form_from_morph_bundle(morph_bundle):
        form = morph_bundle.Form()
        if form is None:
            return None
        return get_single_str_from_form(form)
    
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

    def get_text(self):
        # just join all the forms
        if self.forms is None:
            return ""
        return "".join(x if x is not None else "" for x in self.forms)
    
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
        for form, morph_type, gloss, pos in zip(
            self.forms, self.morph_types, self.glosses, self.poses,
        ):
            morph = WordFormMorpheme(form, morph_type, gloss, pos, self.tag_dict)
            res.append(morph)
        return res

    def __eq__(self, other):
        if type(other) is not WordForm:
            return NotImplemented
        return repr(self) == repr(other)
    
    def __hash__(self):
        return hash(repr(self))


class WordFormMorpheme:
    def __init__(self, form, morph_type, gloss, pos, tag_dict):
        assert type(tag_dict) is TagDict, type(tag_dict)
        self.tag_dict = tag_dict
        self.form = form
        self.morph_type = morph_type
        self.gloss = gloss
        self.pos = pos

    def __repr__(self):
        return "<WordFormMorpheme \"{}\" ({}) = ({}) \"{}\">".format(self.form, self.morph_type, self.pos, self.gloss)

    def __eq__(self, other):
        if type(other) is not WordFormMorpheme:
            return NotImplemented
        return repr(self) == repr(other)
    
    def __hash__(self):
        return hash(repr(self))
