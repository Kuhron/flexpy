from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexPronunciation(Rt):
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

    def CVPattern(self):
        """Gets the child objects which have short tag of `CVPattern`, long tag of `CVPattern`"""
        return get_child_object(self.el, "CVPattern", self.tag_dict)

    def Form(self):
        """Gets the child objects which have short tag of `Form`, long tag of `Form`"""
        return get_child_object(self.el, "Form", self.tag_dict)

    def Location(self):
        """Gets the child objects which have short tag of `Location`, long tag of `Location`"""
        return get_child_object(self.el, "Location", self.tag_dict)

    def Tone(self):
        """Gets the child objects which have short tag of `Tone`, long tag of `Tone`"""
        return get_child_object(self.el, "Tone", self.tag_dict)
