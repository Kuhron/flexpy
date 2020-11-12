from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtText(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Abbreviation(self):
        return get_child_object(self.el, "Abbreviation", self.tag_dict)

    def Contents(self):
        return get_child_object(self.el, "Contents", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Description(self):
        return get_child_object(self.el, "Description", self.tag_dict)

    def IsTranslated(self):
        return get_child_object(self.el, "IsTranslated", self.tag_dict)

    def MediaFiles(self):
        return get_child_object(self.el, "MediaFiles", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def Source(self):
        return get_child_object(self.el, "Source", self.tag_dict)
