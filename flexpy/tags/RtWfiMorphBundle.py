from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiMorphBundle(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Form = get_child_object(self.rt, "Form", self.tag_dict)
        self.Morph = get_child_object(self.rt, "Morph", self.tag_dict)
        self.Msa = get_child_object(self.rt, "Msa", self.tag_dict)
        self.Sense = get_child_object(self.rt, "Sense", self.tag_dict)
