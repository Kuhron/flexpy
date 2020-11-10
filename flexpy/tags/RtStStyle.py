from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStStyle(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.BasedOn = get_child_object(self.el, "BasedOn", self.tag_dict)
        self.Context = get_child_object(self.el, "Context", self.tag_dict)
        self.Function = get_child_object(self.el, "Function", self.tag_dict)
        self.IsBuiltIn = get_child_object(self.el, "IsBuiltIn", self.tag_dict)
        self.IsModified = get_child_object(self.el, "IsModified", self.tag_dict)
        self.IsPublishedTextStyle = get_child_object(self.el, "IsPublishedTextStyle", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.Next = get_child_object(self.el, "Next", self.tag_dict)
        self.Rules = get_child_object(self.el, "Rules", self.tag_dict)
        self.Structure = get_child_object(self.el, "Structure", self.tag_dict)
        self.Type = get_child_object(self.el, "Type", self.tag_dict)
        self.Usage = get_child_object(self.el, "Usage", self.tag_dict)
        self.UserLevel = get_child_object(self.el, "UserLevel", self.tag_dict)
