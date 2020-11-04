from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmRow(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Cells = get_child_object(self.rt, "Cells", self.rt_dict)
