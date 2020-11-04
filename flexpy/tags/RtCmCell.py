from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmCell(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Contents = get_child_object(self.rt, "Contents", self.rt_dict)
