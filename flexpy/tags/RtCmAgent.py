from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmAgent(Rt):
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

    def Approves(self):
        """Gets the child objects which have short tag of `Approves`, long tag of `Approves`"""
        return get_child_object(self.el, "Approves", self.tag_dict)

    def Disapproves(self):
        """Gets the child objects which have short tag of `Disapproves`, long tag of `Disapproves`"""
        return get_child_object(self.el, "Disapproves", self.tag_dict)

    def Human(self):
        """Gets the child objects which have short tag of `Human`, long tag of `Human`"""
        return get_child_object(self.el, "Human", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def Version(self):
        """Gets the child objects which have short tag of `Version`, long tag of `Version`"""
        return get_child_object(self.el, "Version", self.tag_dict)
