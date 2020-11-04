from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStText(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.Paragraphs = get_child_object(self.rt, "Paragraphs", self.rt_dict)
        self.RightToLeft = get_child_object(self.rt, "RightToLeft", self.rt_dict)
