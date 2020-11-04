from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmResource(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.Version = get_child_object(self.rt, "Version", self.rt_dict)
