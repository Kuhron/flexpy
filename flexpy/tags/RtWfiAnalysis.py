from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtWfiAnalysis(Rt):
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

    def Category(self):
        """Gets the child objects which have short tag of `Category`, long tag of `Category`"""
        return get_child_object(self.el, "Category", self.tag_dict)

    def Evaluations(self):
        """Gets the child objects which have short tag of `Evaluations`, long tag of `Evaluations`"""
        return get_child_object(self.el, "Evaluations", self.tag_dict)

    def Meanings(self):
        """Gets the child objects which have short tag of `Meanings`, long tag of `Meanings`"""
        return get_child_object(self.el, "Meanings", self.tag_dict)

    def MorphBundles(self):
        """Gets the child objects which have short tag of `MorphBundles`, long tag of `MorphBundles`"""
        return get_child_object(self.el, "MorphBundles", self.tag_dict)
