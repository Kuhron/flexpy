from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhBdryMarker(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Codes = get_child_object(self.rt, "Codes", self.rt_dict)
        self.Description = get_child_object(self.rt, "Description", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
