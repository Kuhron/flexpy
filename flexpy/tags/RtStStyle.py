from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStStyle(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Context = get_child_object(self.rt, "Context", self.tag_dict)
        self.Function = get_child_object(self.rt, "Function", self.tag_dict)
        self.IsBuiltIn = get_child_object(self.rt, "IsBuiltIn", self.tag_dict)
        self.IsModified = get_child_object(self.rt, "IsModified", self.tag_dict)
        self.IsPublishedTextStyle = get_child_object(self.rt, "IsPublishedTextStyle", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.Rules = get_child_object(self.rt, "Rules", self.tag_dict)
        self.Structure = get_child_object(self.rt, "Structure", self.tag_dict)
        self.Type = get_child_object(self.rt, "Type", self.tag_dict)
        self.Usage = get_child_object(self.rt, "Usage", self.tag_dict)
        self.UserLevel = get_child_object(self.rt, "UserLevel", self.tag_dict)
