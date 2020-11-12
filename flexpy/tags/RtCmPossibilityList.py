from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmPossibilityList(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Abbreviation(self):
        return get_child_object(self.el, "Abbreviation", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Depth(self):
        return get_child_object(self.el, "Depth", self.tag_dict)

    def Description(self):
        return get_child_object(self.el, "Description", self.tag_dict)

    def DisplayOption(self):
        return get_child_object(self.el, "DisplayOption", self.tag_dict)

    def HelpFile(self):
        return get_child_object(self.el, "HelpFile", self.tag_dict)

    def IsClosed(self):
        return get_child_object(self.el, "IsClosed", self.tag_dict)

    def IsSorted(self):
        return get_child_object(self.el, "IsSorted", self.tag_dict)

    def IsVernacular(self):
        return get_child_object(self.el, "IsVernacular", self.tag_dict)

    def ItemClsid(self):
        return get_child_object(self.el, "ItemClsid", self.tag_dict)

    def ListVersion(self):
        return get_child_object(self.el, "ListVersion", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def Possibilities(self):
        return get_child_object(self.el, "Possibilities", self.tag_dict)

    def PreventChoiceAboveLevel(self):
        return get_child_object(self.el, "PreventChoiceAboveLevel", self.tag_dict)

    def PreventDuplicates(self):
        return get_child_object(self.el, "PreventDuplicates", self.tag_dict)

    def PreventNodeChoices(self):
        return get_child_object(self.el, "PreventNodeChoices", self.tag_dict)

    def UseExtendedFields(self):
        return get_child_object(self.el, "UseExtendedFields", self.tag_dict)

    def WsSelector(self):
        return get_child_object(self.el, "WsSelector", self.tag_dict)
