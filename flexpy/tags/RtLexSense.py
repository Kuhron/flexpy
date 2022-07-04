from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexSense(Rt):
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

    def Definition(self):
        """Gets the child objects which have short tag of `Definition`, long tag of `Definition`"""
        return get_child_object(self.el, "Definition", self.tag_dict)

    def DialectLabels(self):
        """Gets the child objects which have short tag of `DialectLabels`, long tag of `DialectLabels`"""
        return get_child_object(self.el, "DialectLabels", self.tag_dict)

    def Examples(self):
        """Gets the child objects which have short tag of `Examples`, long tag of `Examples`"""
        return get_child_object(self.el, "Examples", self.tag_dict)

    def GeneralNote(self):
        """Gets the child objects which have short tag of `GeneralNote`, long tag of `GeneralNote`"""
        return get_child_object(self.el, "GeneralNote", self.tag_dict)

    def Gloss(self):
        """Gets the child objects which have short tag of `Gloss`, long tag of `Gloss`"""
        return get_child_object(self.el, "Gloss", self.tag_dict)

    def GrammarNote(self):
        """Gets the child objects which have short tag of `GrammarNote`, long tag of `GrammarNote`"""
        return get_child_object(self.el, "GrammarNote", self.tag_dict)

    def ImportResidue(self):
        """Gets the child objects which have short tag of `ImportResidue`, long tag of `ImportResidue`"""
        return get_child_object(self.el, "ImportResidue", self.tag_dict)

    def LiftResidue(self):
        """Gets the child objects which have short tag of `LiftResidue`, long tag of `LiftResidue`"""
        return get_child_object(self.el, "LiftResidue", self.tag_dict)

    def MorphoSyntaxAnalysis(self):
        """Gets the child objects which have short tag of `MorphoSyntaxAnalysis`, long tag of `MorphoSyntaxAnalysis`"""
        return get_child_object(self.el, "MorphoSyntaxAnalysis", self.tag_dict)

    def Restrictions(self):
        """Gets the child objects which have short tag of `Restrictions`, long tag of `Restrictions`"""
        return get_child_object(self.el, "Restrictions", self.tag_dict)

    def ReversalEntries(self):
        """Gets the child objects which have short tag of `ReversalEntries`, long tag of `ReversalEntries`"""
        return get_child_object(self.el, "ReversalEntries", self.tag_dict)

    def ScientificName(self):
        """Gets the child objects which have short tag of `ScientificName`, long tag of `ScientificName`"""
        return get_child_object(self.el, "ScientificName", self.tag_dict)

    def SemanticDomains(self):
        """Gets the child objects which have short tag of `SemanticDomains`, long tag of `SemanticDomains`"""
        return get_child_object(self.el, "SemanticDomains", self.tag_dict)

    def SemanticsNote(self):
        """Gets the child objects which have short tag of `SemanticsNote`, long tag of `SemanticsNote`"""
        return get_child_object(self.el, "SemanticsNote", self.tag_dict)

    def Senses(self):
        """Gets the child objects which have short tag of `Senses`, long tag of `Senses`"""
        return get_child_object(self.el, "Senses", self.tag_dict)

    def Source(self):
        """Gets the child objects which have short tag of `Source`, long tag of `Source`"""
        return get_child_object(self.el, "Source", self.tag_dict)
