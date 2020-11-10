from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStTxtPara(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.ParseIsCurrent = get_child_object(self.rt, "ParseIsCurrent", self.tag_dict)
