from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtPhPhonData(Rt):
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

    def NaturalClasses(self):
        """Gets the child objects which have short tag of `NaturalClasses`, long tag of `NaturalClasses`"""
        return get_child_object(self.el, "NaturalClasses", self.tag_dict)

    def PhonRuleFeats(self):
        """Gets the child objects which have short tag of `PhonRuleFeats`, long tag of `PhonRuleFeats`"""
        return get_child_object(self.el, "PhonRuleFeats", self.tag_dict)

    def PhonemeSets(self):
        """Gets the child objects which have short tag of `PhonemeSets`, long tag of `PhonemeSets`"""
        return get_child_object(self.el, "PhonemeSets", self.tag_dict)
