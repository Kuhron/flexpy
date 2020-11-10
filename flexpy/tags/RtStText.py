from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStText(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.Paragraphs = get_child_object(self.rt, "Paragraphs", self.tag_dict)
        self.RightToLeft = get_child_object(self.rt, "RightToLeft", self.tag_dict)
