from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiAnalysis(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Category = get_child_object(self.rt, "Category", self.tag_dict)
        self.Evaluations = get_child_object(self.rt, "Evaluations", self.tag_dict)
        self.Meanings = get_child_object(self.rt, "Meanings", self.tag_dict)
        self.MorphBundles = get_child_object(self.rt, "MorphBundles", self.tag_dict)
