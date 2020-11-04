from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmOverlay(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.PossItems = get_child_object(self.rt, "PossItems", self.rt_dict)
        self.PossList = get_child_object(self.rt, "PossList", self.rt_dict)
