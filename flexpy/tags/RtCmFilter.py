from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmFilter(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def App(self):
        return get_child_object(self.el, "App", self.tag_dict)

    def ClassId(self):
        return get_child_object(self.el, "ClassId", self.tag_dict)

    def ColumnInfo(self):
        return get_child_object(self.el, "ColumnInfo", self.tag_dict)

    def FieldId(self):
        return get_child_object(self.el, "FieldId", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def PromptText(self):
        return get_child_object(self.el, "PromptText", self.tag_dict)

    def Rows(self):
        return get_child_object(self.el, "Rows", self.tag_dict)

    def ShowPrompt(self):
        return get_child_object(self.el, "ShowPrompt", self.tag_dict)

    def Type(self):
        return get_child_object(self.el, "Type", self.tag_dict)
