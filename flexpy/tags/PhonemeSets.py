from flexpy.NonRtTag import NonRtTag
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class PhonemeSets(NonRtTag):
    """A class for FLEx XML elements with the tag PhonemeSets

    :param el: the `xml.etree.ElementTree.Element` object
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, parent_el=None, tag_dict=None):
        super().__init__(el, parent_el=parent_el, tag_dict=tag_dict)
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.fp = self.el.attrib.get("fp")

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def RtPhPhonemeSet(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtPhPhonemeSet`, class name of `PhPhonemeSet`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="PhPhonemeSet")
