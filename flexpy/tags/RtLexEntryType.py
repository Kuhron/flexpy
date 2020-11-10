from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntryType(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Abbreviation = get_child_object(self.rt, "Abbreviation", self.tag_dict)
        self.BackColor = get_child_object(self.rt, "BackColor", self.tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.Description = get_child_object(self.rt, "Description", self.tag_dict)
        self.Discussion = get_child_object(self.rt, "Discussion", self.tag_dict)
        self.ForeColor = get_child_object(self.rt, "ForeColor", self.tag_dict)
        self.Hidden = get_child_object(self.rt, "Hidden", self.tag_dict)
        self.IsProtected = get_child_object(self.rt, "IsProtected", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.ReverseAbbr = get_child_object(self.rt, "ReverseAbbr", self.tag_dict)
        self.ReverseName = get_child_object(self.rt, "ReverseName", self.tag_dict)
        self.SortSpec = get_child_object(self.rt, "SortSpec", self.tag_dict)
        self.UnderColor = get_child_object(self.rt, "UnderColor", self.tag_dict)
        self.UnderStyle = get_child_object(self.rt, "UnderStyle", self.tag_dict)
