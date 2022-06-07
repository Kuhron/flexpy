from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntryType(Rt):
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

    def BackColor(self):
        """Gets the child objects which have short tag of `BackColor`, long tag of `BackColor`"""
        return get_child_object(self.el, "BackColor", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Description(self):
        """Gets the child objects which have short tag of `Description`, long tag of `Description`"""
        return get_child_object(self.el, "Description", self.tag_dict)

    def Discussion(self):
        """Gets the child objects which have short tag of `Discussion`, long tag of `Discussion`"""
        return get_child_object(self.el, "Discussion", self.tag_dict)

    def ForeColor(self):
        """Gets the child objects which have short tag of `ForeColor`, long tag of `ForeColor`"""
        return get_child_object(self.el, "ForeColor", self.tag_dict)

    def Hidden(self):
        """Gets the child objects which have short tag of `Hidden`, long tag of `Hidden`"""
        return get_child_object(self.el, "Hidden", self.tag_dict)

    def IsProtected(self):
        """Gets the child objects which have short tag of `IsProtected`, long tag of `IsProtected`"""
        return get_child_object(self.el, "IsProtected", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def ReverseAbbr(self):
        """Gets the child objects which have short tag of `ReverseAbbr`, long tag of `ReverseAbbr`"""
        return get_child_object(self.el, "ReverseAbbr", self.tag_dict)

    def ReverseName(self):
        """Gets the child objects which have short tag of `ReverseName`, long tag of `ReverseName`"""
        return get_child_object(self.el, "ReverseName", self.tag_dict)

    def SortSpec(self):
        """Gets the child objects which have short tag of `SortSpec`, long tag of `SortSpec`"""
        return get_child_object(self.el, "SortSpec", self.tag_dict)

    def UnderColor(self):
        """Gets the child objects which have short tag of `UnderColor`, long tag of `UnderColor`"""
        return get_child_object(self.el, "UnderColor", self.tag_dict)

    def UnderStyle(self):
        """Gets the child objects which have short tag of `UnderStyle`, long tag of `UnderStyle`"""
        return get_child_object(self.el, "UnderStyle", self.tag_dict)
