from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtMoMorphData(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.ParserParameters = get_child_object(self.rt, "ParserParameters", self.rt_dict)
        self.ProdRestrict = get_child_object(self.rt, "ProdRestrict", self.rt_dict)
