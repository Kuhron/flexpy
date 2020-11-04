from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmAnthroItem(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Abbreviation = get_child_object(self.rt, "Abbreviation", self.rt_dict)
        self.BackColor = get_child_object(self.rt, "BackColor", self.rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.Discussion = get_child_object(self.rt, "Discussion", self.rt_dict)
        self.ForeColor = get_child_object(self.rt, "ForeColor", self.rt_dict)
        self.HelpId = get_child_object(self.rt, "HelpId", self.rt_dict)
        self.Hidden = get_child_object(self.rt, "Hidden", self.rt_dict)
        self.IsProtected = get_child_object(self.rt, "IsProtected", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.SortSpec = get_child_object(self.rt, "SortSpec", self.rt_dict)
        self.UnderColor = get_child_object(self.rt, "UnderColor", self.rt_dict)
        self.UnderStyle = get_child_object(self.rt, "UnderStyle", self.rt_dict)
