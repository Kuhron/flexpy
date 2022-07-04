from flexpy.NonRtTag import NonRtTag
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Analyses(NonRtTag):
    """A class for FLEx XML elements with the tag Analyses

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

    def RtPunctuationForm(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtPunctuationForm`, class name of `PunctuationForm`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="PunctuationForm")

    def RtWfiAnalysis(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtWfiAnalysis`, class name of `WfiAnalysis`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="WfiAnalysis")

    def RtWfiGloss(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtWfiGloss`, class name of `WfiGloss`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="WfiGloss")

    def RtWfiWordform(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtWfiWordform`, class name of `WfiWordform`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="WfiWordform")
