from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmFilter(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.App = get_child_object(self.el, "App", self.tag_dict)
        self.ClassId = get_child_object(self.el, "ClassId", self.tag_dict)
        self.ColumnInfo = get_child_object(self.el, "ColumnInfo", self.tag_dict)
        self.FieldId = get_child_object(self.el, "FieldId", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.PromptText = get_child_object(self.el, "PromptText", self.tag_dict)
        self.Rows = get_child_object(self.el, "Rows", self.tag_dict)
        self.ShowPrompt = get_child_object(self.el, "ShowPrompt", self.tag_dict)
        self.Type = get_child_object(self.el, "Type", self.tag_dict)
