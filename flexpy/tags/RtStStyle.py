from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtStStyle(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def BasedOn(self):
        return get_child_object(self.el, "BasedOn", self.tag_dict)

    def Context(self):
        return get_child_object(self.el, "Context", self.tag_dict)

    def Function(self):
        return get_child_object(self.el, "Function", self.tag_dict)

    def IsBuiltIn(self):
        return get_child_object(self.el, "IsBuiltIn", self.tag_dict)

    def IsModified(self):
        return get_child_object(self.el, "IsModified", self.tag_dict)

    def IsPublishedTextStyle(self):
        return get_child_object(self.el, "IsPublishedTextStyle", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def Next(self):
        return get_child_object(self.el, "Next", self.tag_dict)

    def Rules(self):
        return get_child_object(self.el, "Rules", self.tag_dict)

    def Structure(self):
        return get_child_object(self.el, "Structure", self.tag_dict)

    def Type(self):
        return get_child_object(self.el, "Type", self.tag_dict)

    def Usage(self):
        return get_child_object(self.el, "Usage", self.tag_dict)

    def UserLevel(self):
        return get_child_object(self.el, "UserLevel", self.tag_dict)
