from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoEndoCompound(Rt):
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

    def Description(self):
        """Gets the child objects which have short tag of `Description`, long tag of `Description`"""
        return get_child_object(self.el, "Description", self.tag_dict)

    def Disabled(self):
        """Gets the child objects which have short tag of `Disabled`, long tag of `Disabled`"""
        return get_child_object(self.el, "Disabled", self.tag_dict)

    def HeadLast(self):
        """Gets the child objects which have short tag of `HeadLast`, long tag of `HeadLast`"""
        return get_child_object(self.el, "HeadLast", self.tag_dict)

    def LeftMsa(self):
        """Gets the child objects which have short tag of `LeftMsa`, long tag of `LeftMsa`"""
        return get_child_object(self.el, "LeftMsa", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def OverridingMsa(self):
        """Gets the child objects which have short tag of `OverridingMsa`, long tag of `OverridingMsa`"""
        return get_child_object(self.el, "OverridingMsa", self.tag_dict)

    def RightMsa(self):
        """Gets the child objects which have short tag of `RightMsa`, long tag of `RightMsa`"""
        return get_child_object(self.el, "RightMsa", self.tag_dict)
