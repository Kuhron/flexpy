from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmFilter(Rt):
    """A class for FLEx XML elements with the tag rt
    :param el: the `xml.etree.ElementTree.Element object`
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def App(self):
        """Gets the child objects which have short tag of `App`, long tag of `App`"""
        return get_child_object(self.el, "App", self.tag_dict)

    def ClassId(self):
        """Gets the child objects which have short tag of `ClassId`, long tag of `ClassId`"""
        return get_child_object(self.el, "ClassId", self.tag_dict)

    def ColumnInfo(self):
        """Gets the child objects which have short tag of `ColumnInfo`, long tag of `ColumnInfo`"""
        return get_child_object(self.el, "ColumnInfo", self.tag_dict)

    def FieldId(self):
        """Gets the child objects which have short tag of `FieldId`, long tag of `FieldId`"""
        return get_child_object(self.el, "FieldId", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def PromptText(self):
        """Gets the child objects which have short tag of `PromptText`, long tag of `PromptText`"""
        return get_child_object(self.el, "PromptText", self.tag_dict)

    def Rows(self):
        """Gets the child objects which have short tag of `Rows`, long tag of `Rows`"""
        return get_child_object(self.el, "Rows", self.tag_dict)

    def ShowPrompt(self):
        """Gets the child objects which have short tag of `ShowPrompt`, long tag of `ShowPrompt`"""
        return get_child_object(self.el, "ShowPrompt", self.tag_dict)

    def Type(self):
        """Gets the child objects which have short tag of `Type`, long tag of `Type`"""
        return get_child_object(self.el, "Type", self.tag_dict)
