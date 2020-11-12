from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtRnResearchNbk(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def RecTypes(self):
        return get_child_object(self.el, "RecTypes", self.tag_dict)
