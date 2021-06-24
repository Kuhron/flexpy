from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexSense(Rt):
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

    def Definition(self):
        """Gets the child objects which have short tag of `Definition`, long tag of `Definition`"""
        return get_child_object(self.el, "Definition", self.tag_dict)

    def Gloss(self):
        """Gets the child objects which have short tag of `Gloss`, long tag of `Gloss`"""
        return get_child_object(self.el, "Gloss", self.tag_dict)

    def MorphoSyntaxAnalysis(self):
        """Gets the child objects which have short tag of `MorphoSyntaxAnalysis`, long tag of `MorphoSyntaxAnalysis`"""
        return get_child_object(self.el, "MorphoSyntaxAnalysis", self.tag_dict)

    def ScientificName(self):
        """Gets the child objects which have short tag of `ScientificName`, long tag of `ScientificName`"""
        return get_child_object(self.el, "ScientificName", self.tag_dict)

    def SemanticDomains(self):
        """Gets the child objects which have short tag of `SemanticDomains`, long tag of `SemanticDomains`"""
        return get_child_object(self.el, "SemanticDomains", self.tag_dict)

    def Source(self):
        """Gets the child objects which have short tag of `Source`, long tag of `Source`"""
        return get_child_object(self.el, "Source", self.tag_dict)
