from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmPossibilityList(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Abbreviation = get_child_object(self.rt, "Abbreviation", self.rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.Depth = get_child_object(self.rt, "Depth", self.rt_dict)
        self.DisplayOption = get_child_object(self.rt, "DisplayOption", self.rt_dict)
        self.IsClosed = get_child_object(self.rt, "IsClosed", self.rt_dict)
        self.IsSorted = get_child_object(self.rt, "IsSorted", self.rt_dict)
        self.IsVernacular = get_child_object(self.rt, "IsVernacular", self.rt_dict)
        self.ItemClsid = get_child_object(self.rt, "ItemClsid", self.rt_dict)
        self.ListVersion = get_child_object(self.rt, "ListVersion", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.Possibilities = get_child_object(self.rt, "Possibilities", self.rt_dict)
        self.PreventChoiceAboveLevel = get_child_object(self.rt, "PreventChoiceAboveLevel", self.rt_dict)
        self.PreventDuplicates = get_child_object(self.rt, "PreventDuplicates", self.rt_dict)
        self.PreventNodeChoices = get_child_object(self.rt, "PreventNodeChoices", self.rt_dict)
        self.UseExtendedFields = get_child_object(self.rt, "UseExtendedFields", self.rt_dict)
        self.WsSelector = get_child_object(self.rt, "WsSelector", self.rt_dict)
