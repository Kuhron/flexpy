from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtRnGenericRec(Rt):
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

    def DateOfEvent(self):
        return get_child_object(self.el, "DateOfEvent", self.tag_dict)

    def Researchers(self):
        return get_child_object(self.el, "Researchers", self.tag_dict)

    def Text(self):
        return get_child_object(self.el, "Text", self.tag_dict)

    def Type(self):
        return get_child_object(self.el, "Type", self.tag_dict)
