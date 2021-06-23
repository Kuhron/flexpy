from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoMorphData(Rt):
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

    def ParserParameters(self):
        """Gets the child objects which have short tag of `ParserParameters`, long tag of `ParserParameters`"""
        return get_child_object(self.el, "ParserParameters", self.tag_dict)

    def ProdRestrict(self):
        """Gets the child objects which have short tag of `ProdRestrict`, long tag of `ProdRestrict`"""
        return get_child_object(self.el, "ProdRestrict", self.tag_dict)
