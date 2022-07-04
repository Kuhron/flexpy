from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexExampleSentence(Rt):
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

    def Example(self):
        """Gets the child objects which have short tag of `Example`, long tag of `Example`"""
        return get_child_object(self.el, "Example", self.tag_dict)

    def Reference(self):
        """Gets the child objects which have short tag of `Reference`, long tag of `Reference`"""
        return get_child_object(self.el, "Reference", self.tag_dict)

    def Translations(self):
        """Gets the child objects which have short tag of `Translations`, long tag of `Translations`"""
        return get_child_object(self.el, "Translations", self.tag_dict)
