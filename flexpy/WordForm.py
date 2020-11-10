from flexpy.TagDict import TagDict
from flexpy.tags.RtWfiAnalysis import RtWfiAnalysis


class WordForm:
    def __init__(self, rt_wfi_analysis, tag_dict):
        assert type(rt_wfi_analysis) is RtWfiAnalysis, type(rt_wfi_analysis)
        assert type(tag_dict) is TagDict, type(tag_dict)
        self.rt_wfi_analysis = rt_wfi_analysis
        self.tag_dict = tag_dict
        self.form = self.create_form()
        self.gloss = self.create_gloss()
        self.pos = self.create_pos()
    
    def create_form(self):
        morph_bundles = self.rt_wfi_analysis.MorphBundles
        rt_wfi_morph_bundle = morph_bundles.RtWfiMorphBundle
        for morph_bundle in rt_wfi_morph_bundle:
            form = morph_bundle.Form
            morph = morph_bundle.Morph
            msa = morph_bundle.Msa
            sense = morph_bundle.Sense
            print(form, morph, msa, sense)

        raise NotImplementedError
    
    def create_gloss(self):
        meanings = self.rt_wfi_analysis.Meanings
        raise NotImplementedError

    def create_pos(self):
        category = self.rt_wfi_analysis.Category
        raise NotImplementedError