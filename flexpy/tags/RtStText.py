from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStText(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Paragraphs = get_child_object(self.el, "Paragraphs", self.tag_dict)
        self.RightToLeft = get_child_object(self.el, "RightToLeft", self.tag_dict)