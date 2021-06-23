from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtStText(Rt):
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

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Paragraphs(self):
        """Gets the child objects which have short tag of `Paragraphs`, long tag of `Paragraphs`"""
        return get_child_object(self.el, "Paragraphs", self.tag_dict)

    def RightToLeft(self):
        """Gets the child objects which have short tag of `RightToLeft`, long tag of `RightToLeft`"""
        return get_child_object(self.el, "RightToLeft", self.tag_dict)
