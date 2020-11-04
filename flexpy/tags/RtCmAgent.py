from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmAgent(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Approves = get_child_object(self.rt, "Approves", self.rt_dict)
        self.Disapproves = get_child_object(self.rt, "Disapproves", self.rt_dict)
        self.Human = get_child_object(self.rt, "Human", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.Notes = get_child_object(self.rt, "Notes", self.rt_dict)
        self.Version = get_child_object(self.rt, "Version", self.rt_dict)
