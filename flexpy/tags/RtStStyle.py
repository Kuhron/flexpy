from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStStyle(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Context = get_child_object(self.rt, "Context", self.rt_dict)
        self.Function = get_child_object(self.rt, "Function", self.rt_dict)
        self.IsBuiltIn = get_child_object(self.rt, "IsBuiltIn", self.rt_dict)
        self.IsModified = get_child_object(self.rt, "IsModified", self.rt_dict)
        self.IsPublishedTextStyle = get_child_object(self.rt, "IsPublishedTextStyle", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.Rules = get_child_object(self.rt, "Rules", self.rt_dict)
        self.Structure = get_child_object(self.rt, "Structure", self.rt_dict)
        self.Type = get_child_object(self.rt, "Type", self.rt_dict)
        self.Usage = get_child_object(self.rt, "Usage", self.rt_dict)
        self.UserLevel = get_child_object(self.rt, "UserLevel", self.rt_dict)
