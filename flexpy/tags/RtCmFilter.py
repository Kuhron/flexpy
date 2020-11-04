from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmFilter(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.App = get_child_object(self.rt, "App", self.rt_dict)
        self.ClassId = get_child_object(self.rt, "ClassId", self.rt_dict)
        self.ColumnInfo = get_child_object(self.rt, "ColumnInfo", self.rt_dict)
        self.FieldId = get_child_object(self.rt, "FieldId", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.Rows = get_child_object(self.rt, "Rows", self.rt_dict)
        self.ShowPrompt = get_child_object(self.rt, "ShowPrompt", self.rt_dict)
        self.Type = get_child_object(self.rt, "Type", self.rt_dict)
