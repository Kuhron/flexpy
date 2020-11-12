raise Exception("do not use")

from flexpy.FlexPyUtil import get_strs_from_form

from flexpy.tags.RtWfiMorphBundle import RtWfiMorphBundle


class Morpheme:
    def __init__(self, form, morph_type, pos, gloss):
        assert type(form) is str or form is None, form
        self.form = form
        assert type(morph_type) is str or morph_type is None, morph_type
        self.morph_type = morph_type
        assert type(pos) is str or pos is None, pos
        self.pos = pos
        assert type(gloss) is str or gloss is None, gloss
        self.gloss = gloss

    def __repr__(self):
        return "<Morpheme \"{}\" ({}) = ({}) \"{}\">".format(self.form, self.morph_type, self.pos, self.gloss)
    
    # @staticmethod
    # def from_rt_wfi_morph_bundle(rt_wfi_morph_bundle):
    #     assert type(rt_wfi_morph_bundle) is RtWfiMorphBundle, type(rt_wfi_morph_bundle)
    #     form = Morpheme.get_form_from_morph_bundle(rt_wfi_morph_bundle)
    #     morph_type = Morpheme.get_morph_type_from_morph_bundle(rt_wfi_morph_bundle)
    #     pos = Morpheme.get_pos_name_from_morph_bundle(rt_wfi_morph_bundle)
    #     gloss = Morpheme.get_gloss_from_morph_bundle(rt_wfi_morph_bundle)
    #     return Morpheme(form, morph_type, pos, gloss)
