from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiWordform(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Checksum = get_child_object(self.rt, "Checksum", self.rt_dict)
        self.Form = get_child_object(self.rt, "Form", self.rt_dict)
        self.SpellingStatus = get_child_object(self.rt, "SpellingStatus", self.rt_dict)
