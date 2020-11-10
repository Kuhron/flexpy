from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmFilter(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.App = get_child_object(self.el, "App", self.tag_dict)
        self.ClassId = get_child_object(self.el, "ClassId", self.tag_dict)
        self.ColumnInfo = get_child_object(self.el, "ColumnInfo", self.tag_dict)
        self.FieldId = get_child_object(self.el, "FieldId", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.PromptText = get_child_object(self.el, "PromptText", self.tag_dict)
        self.Rows = get_child_object(self.el, "Rows", self.tag_dict)
        self.ShowPrompt = get_child_object(self.el, "ShowPrompt", self.tag_dict)
        self.Type = get_child_object(self.el, "Type", self.tag_dict)
