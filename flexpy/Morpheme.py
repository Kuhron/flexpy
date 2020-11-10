from flexpy.tags.RtWfiMorphBundle import RtWfiMorphBundle


class Morpheme:
    def __init__(self, form, morph_type, pos, gloss):
        assert type(form) is str
        self.form = form
        assert type(morph_type) is str
        self.morph_type = morph_type
        assert type(pos) is str
        self.pos = pos
        assert type(gloss) is str
        self.gloss = gloss
    
    @staticmethod
    def from_rt_wfi_morph_bundle(rt_wfi_morph_bundle):
        assert type(rt_wfi_morph_bundle) is RtWfiMorphBundle, type(rt_wfi_morph_bundle)
        