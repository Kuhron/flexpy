from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmPossibilityList(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Abbreviation = get_child_object(self.rt, "Abbreviation", self.tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.Depth = get_child_object(self.rt, "Depth", self.tag_dict)
        self.DisplayOption = get_child_object(self.rt, "DisplayOption", self.tag_dict)
        self.IsClosed = get_child_object(self.rt, "IsClosed", self.tag_dict)
        self.IsSorted = get_child_object(self.rt, "IsSorted", self.tag_dict)
        self.IsVernacular = get_child_object(self.rt, "IsVernacular", self.tag_dict)
        self.ItemClsid = get_child_object(self.rt, "ItemClsid", self.tag_dict)
        self.ListVersion = get_child_object(self.rt, "ListVersion", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.Possibilities = get_child_object(self.rt, "Possibilities", self.tag_dict)
        self.PreventChoiceAboveLevel = get_child_object(self.rt, "PreventChoiceAboveLevel", self.tag_dict)
        self.PreventDuplicates = get_child_object(self.rt, "PreventDuplicates", self.tag_dict)
        self.PreventNodeChoices = get_child_object(self.rt, "PreventNodeChoices", self.tag_dict)
        self.UseExtendedFields = get_child_object(self.rt, "UseExtendedFields", self.tag_dict)
        self.WsSelector = get_child_object(self.rt, "WsSelector", self.tag_dict)
