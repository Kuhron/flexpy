from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhPhoneme(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Codes = get_child_object(self.rt, "Codes", self.tag_dict)
        self.Description = get_child_object(self.rt, "Description", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
