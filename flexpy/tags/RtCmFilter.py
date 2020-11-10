from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmFilter(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.App = get_child_object(self.rt, "App", self.tag_dict)
        self.ClassId = get_child_object(self.rt, "ClassId", self.tag_dict)
        self.ColumnInfo = get_child_object(self.rt, "ColumnInfo", self.tag_dict)
        self.FieldId = get_child_object(self.rt, "FieldId", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.Rows = get_child_object(self.rt, "Rows", self.tag_dict)
        self.ShowPrompt = get_child_object(self.rt, "ShowPrompt", self.tag_dict)
        self.Type = get_child_object(self.rt, "Type", self.tag_dict)
