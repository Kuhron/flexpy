from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmAgent(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Approves = get_child_object(self.rt, "Approves", self.tag_dict)
        self.Disapproves = get_child_object(self.rt, "Disapproves", self.tag_dict)
        self.Human = get_child_object(self.rt, "Human", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.Notes = get_child_object(self.rt, "Notes", self.tag_dict)
        self.Version = get_child_object(self.rt, "Version", self.tag_dict)
