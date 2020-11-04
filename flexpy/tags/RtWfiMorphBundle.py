from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiMorphBundle(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Form = get_child_object(self.rt, "Form", self.rt_dict)
        self.Morph = get_child_object(self.rt, "Morph", self.rt_dict)
        self.Msa = get_child_object(self.rt, "Msa", self.rt_dict)
        self.Sense = get_child_object(self.rt, "Sense", self.rt_dict)
