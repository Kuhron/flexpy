from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtMoMorphData(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.ParserParameters = get_child_object(self.rt, "ParserParameters", self.tag_dict)
        self.ProdRestrict = get_child_object(self.rt, "ProdRestrict", self.tag_dict)
