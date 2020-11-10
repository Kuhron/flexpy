from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmOverlay(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.PossItems = get_child_object(self.rt, "PossItems", self.tag_dict)
        self.PossList = get_child_object(self.rt, "PossList", self.tag_dict)
