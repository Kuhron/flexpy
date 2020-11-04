from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiAnalysis(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Category = get_child_object(self.rt, "Category", self.rt_dict)
        self.Evaluations = get_child_object(self.rt, "Evaluations", self.rt_dict)
        self.Meanings = get_child_object(self.rt, "Meanings", self.rt_dict)
        self.MorphBundles = get_child_object(self.rt, "MorphBundles", self.rt_dict)
