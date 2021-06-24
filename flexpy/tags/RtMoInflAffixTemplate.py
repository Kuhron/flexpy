from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoInflAffixTemplate(Rt):
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

    def Disabled(self):
        """Gets the child objects which have short tag of `Disabled`, long tag of `Disabled`"""
        return get_child_object(self.el, "Disabled", self.tag_dict)

    def Final(self):
        """Gets the child objects which have short tag of `Final`, long tag of `Final`"""
        return get_child_object(self.el, "Final", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def PrefixSlots(self):
        """Gets the child objects which have short tag of `PrefixSlots`, long tag of `PrefixSlots`"""
        return get_child_object(self.el, "PrefixSlots", self.tag_dict)

    def SuffixSlots(self):
        """Gets the child objects which have short tag of `SuffixSlots`, long tag of `SuffixSlots`"""
        return get_child_object(self.el, "SuffixSlots", self.tag_dict)
