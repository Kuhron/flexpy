raise Exception("do not use")

from flexpy.Morpheme import Morpheme

from flexpy.tags.RtWfiMorphBundle import RtWfiMorphBundle


class WordAnalysis:
    def __init__(self, morphemes):
        self.morphemes = morphemes

    def __repr__(self):
        return "<WordAnalysis morphemes={}>".format(self.morphemes)

    @staticmethod
    def from_rt_wfi_morph_bundles(rt_wfi_morph_bundles):
        assert type(rt_wfi_morph_bundles) is list
        assert all(type(x) is RtWfiMorphBundle for x in rt_wfi_morph_bundles)
        # assert len(rt_wfi_morph_bundles) == 1, "don't know how to deal with analysis with more than one morph bundle"
        morphemes = []
        for rt_wfi_morph_bundle in rt_wfi_morph_bundles:
            morpheme = Morpheme.from_rt_wfi_morph_bundle(rt_wfi_morph_bundle)
            morphemes.append(morpheme)
        return WordAnalysis(morphemes)
