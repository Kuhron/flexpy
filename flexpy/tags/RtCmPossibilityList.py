from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmPossibilityList(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.Abbreviation = get_child_object(self.el, "Abbreviation", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Depth = get_child_object(self.el, "Depth", self.tag_dict)
        self.Description = get_child_object(self.el, "Description", self.tag_dict)
        self.DisplayOption = get_child_object(self.el, "DisplayOption", self.tag_dict)
        self.HelpFile = get_child_object(self.el, "HelpFile", self.tag_dict)
        self.IsClosed = get_child_object(self.el, "IsClosed", self.tag_dict)
        self.IsSorted = get_child_object(self.el, "IsSorted", self.tag_dict)
        self.IsVernacular = get_child_object(self.el, "IsVernacular", self.tag_dict)
        self.ItemClsid = get_child_object(self.el, "ItemClsid", self.tag_dict)
        self.ListVersion = get_child_object(self.el, "ListVersion", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.Possibilities = get_child_object(self.el, "Possibilities", self.tag_dict)
        self.PreventChoiceAboveLevel = get_child_object(self.el, "PreventChoiceAboveLevel", self.tag_dict)
        self.PreventDuplicates = get_child_object(self.el, "PreventDuplicates", self.tag_dict)
        self.PreventNodeChoices = get_child_object(self.el, "PreventNodeChoices", self.tag_dict)
        self.UseExtendedFields = get_child_object(self.el, "UseExtendedFields", self.tag_dict)
        self.WsSelector = get_child_object(self.el, "WsSelector", self.tag_dict)
