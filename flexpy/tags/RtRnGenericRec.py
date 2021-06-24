from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtRnGenericRec(Rt):
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

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DateOfEvent(self):
        """Gets the child objects which have short tag of `DateOfEvent`, long tag of `DateOfEvent`"""
        return get_child_object(self.el, "DateOfEvent", self.tag_dict)

    def Researchers(self):
        """Gets the child objects which have short tag of `Researchers`, long tag of `Researchers`"""
        return get_child_object(self.el, "Researchers", self.tag_dict)

    def Text(self):
        """Gets the child objects which have short tag of `Text`, long tag of `Text`"""
        return get_child_object(self.el, "Text", self.tag_dict)

    def Type(self):
        """Gets the child objects which have short tag of `Type`, long tag of `Type`"""
        return get_child_object(self.el, "Type", self.tag_dict)
