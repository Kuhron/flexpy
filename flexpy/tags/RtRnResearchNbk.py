from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtRnResearchNbk(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.RecTypes = get_child_object(self.rt, "RecTypes", self.rt_dict)
