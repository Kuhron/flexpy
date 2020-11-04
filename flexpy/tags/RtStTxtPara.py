from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStTxtPara(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.ParseIsCurrent = get_child_object(self.rt, "ParseIsCurrent", self.rt_dict)
