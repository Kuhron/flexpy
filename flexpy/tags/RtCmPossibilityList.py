from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmPossibilityList(Rt):
    """A class for FLEx XML elements with the tag rt

    :param el: the `xml.etree.ElementTree.Element` object
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, parent_el=None, tag_dict=None):
        super().__init__(el, parent_el=parent_el, tag_dict=tag_dict)
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Abbreviation(self):
        """Gets the child objects which have short tag of `Abbreviation`, long tag of `Abbreviation`"""
        return get_child_object(self.el, "Abbreviation", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Depth(self):
        """Gets the child objects which have short tag of `Depth`, long tag of `Depth`"""
        return get_child_object(self.el, "Depth", self.tag_dict)

    def Description(self):
        """Gets the child objects which have short tag of `Description`, long tag of `Description`"""
        return get_child_object(self.el, "Description", self.tag_dict)

    def DisplayOption(self):
        """Gets the child objects which have short tag of `DisplayOption`, long tag of `DisplayOption`"""
        return get_child_object(self.el, "DisplayOption", self.tag_dict)

    def HelpFile(self):
        """Gets the child objects which have short tag of `HelpFile`, long tag of `HelpFile`"""
        return get_child_object(self.el, "HelpFile", self.tag_dict)

    def IsClosed(self):
        """Gets the child objects which have short tag of `IsClosed`, long tag of `IsClosed`"""
        return get_child_object(self.el, "IsClosed", self.tag_dict)

    def IsSorted(self):
        """Gets the child objects which have short tag of `IsSorted`, long tag of `IsSorted`"""
        return get_child_object(self.el, "IsSorted", self.tag_dict)

    def IsVernacular(self):
        """Gets the child objects which have short tag of `IsVernacular`, long tag of `IsVernacular`"""
        return get_child_object(self.el, "IsVernacular", self.tag_dict)

    def ItemClsid(self):
        """Gets the child objects which have short tag of `ItemClsid`, long tag of `ItemClsid`"""
        return get_child_object(self.el, "ItemClsid", self.tag_dict)

    def ListVersion(self):
        """Gets the child objects which have short tag of `ListVersion`, long tag of `ListVersion`"""
        return get_child_object(self.el, "ListVersion", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def Possibilities(self):
        """Gets the child objects which have short tag of `Possibilities`, long tag of `Possibilities`"""
        return get_child_object(self.el, "Possibilities", self.tag_dict)

    def PreventChoiceAboveLevel(self):
        """Gets the child objects which have short tag of `PreventChoiceAboveLevel`, long tag of `PreventChoiceAboveLevel`"""
        return get_child_object(self.el, "PreventChoiceAboveLevel", self.tag_dict)

    def PreventDuplicates(self):
        """Gets the child objects which have short tag of `PreventDuplicates`, long tag of `PreventDuplicates`"""
        return get_child_object(self.el, "PreventDuplicates", self.tag_dict)

    def PreventNodeChoices(self):
        """Gets the child objects which have short tag of `PreventNodeChoices`, long tag of `PreventNodeChoices`"""
        return get_child_object(self.el, "PreventNodeChoices", self.tag_dict)

    def UseExtendedFields(self):
        """Gets the child objects which have short tag of `UseExtendedFields`, long tag of `UseExtendedFields`"""
        return get_child_object(self.el, "UseExtendedFields", self.tag_dict)

    def WsSelector(self):
        """Gets the child objects which have short tag of `WsSelector`, long tag of `WsSelector`"""
        return get_child_object(self.el, "WsSelector", self.tag_dict)
