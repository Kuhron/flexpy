from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtText(Rt):
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

    def Contents(self):
        """Gets the child objects which have short tag of `Contents`, long tag of `Contents`"""
        return get_child_object(self.el, "Contents", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Description(self):
        """Gets the child objects which have short tag of `Description`, long tag of `Description`"""
        return get_child_object(self.el, "Description", self.tag_dict)

    def Genres(self):
        """Gets the child objects which have short tag of `Genres`, long tag of `Genres`"""
        return get_child_object(self.el, "Genres", self.tag_dict)

    def IsTranslated(self):
        """Gets the child objects which have short tag of `IsTranslated`, long tag of `IsTranslated`"""
        return get_child_object(self.el, "IsTranslated", self.tag_dict)

    def MediaFiles(self):
        """Gets the child objects which have short tag of `MediaFiles`, long tag of `MediaFiles`"""
        return get_child_object(self.el, "MediaFiles", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def Source(self):
        """Gets the child objects which have short tag of `Source`, long tag of `Source`"""
        return get_child_object(self.el, "Source", self.tag_dict)
