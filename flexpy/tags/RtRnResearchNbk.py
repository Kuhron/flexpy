from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtRnResearchNbk(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.RecTypes = get_child_object(self.el, "RecTypes", self.tag_dict)
