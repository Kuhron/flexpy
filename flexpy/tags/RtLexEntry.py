from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntry(Rt):
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

    def AlternateForms(self):
        """Gets the child objects which have short tag of `AlternateForms`, long tag of `AlternateForms`"""
        return get_child_object(self.el, "AlternateForms", self.tag_dict)

    def Comment(self):
        """Gets the child objects which have short tag of `Comment`, long tag of `Comment`"""
        return get_child_object(self.el, "Comment", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DoNotPublishIn(self):
        """Gets the child objects which have short tag of `DoNotPublishIn`, long tag of `DoNotPublishIn`"""
        return get_child_object(self.el, "DoNotPublishIn", self.tag_dict)

    def DoNotUseForParsing(self):
        """Gets the child objects which have short tag of `DoNotUseForParsing`, long tag of `DoNotUseForParsing`"""
        return get_child_object(self.el, "DoNotUseForParsing", self.tag_dict)

    def EntryRefs(self):
        """Gets the child objects which have short tag of `EntryRefs`, long tag of `EntryRefs`"""
        return get_child_object(self.el, "EntryRefs", self.tag_dict)

    def HomographNumber(self):
        """Gets the child objects which have short tag of `HomographNumber`, long tag of `HomographNumber`"""
        return get_child_object(self.el, "HomographNumber", self.tag_dict)

    def LexemeForm(self):
        """Gets the child objects which have short tag of `LexemeForm`, long tag of `LexemeForm`"""
        return get_child_object(self.el, "LexemeForm", self.tag_dict)

    def MorphoSyntaxAnalyses(self):
        """Gets the child objects which have short tag of `MorphoSyntaxAnalyses`, long tag of `MorphoSyntaxAnalyses`"""
        return get_child_object(self.el, "MorphoSyntaxAnalyses", self.tag_dict)

    def Pronunciations(self):
        """Gets the child objects which have short tag of `Pronunciations`, long tag of `Pronunciations`"""
        return get_child_object(self.el, "Pronunciations", self.tag_dict)

    def Senses(self):
        """Gets the child objects which have short tag of `Senses`, long tag of `Senses`"""
        return get_child_object(self.el, "Senses", self.tag_dict)
