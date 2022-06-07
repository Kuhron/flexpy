from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntryRef(Rt):
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

    def ComplexEntryTypes(self):
        """Gets the child objects which have short tag of `ComplexEntryTypes`, long tag of `ComplexEntryTypes`"""
        return get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)

    def ComponentLexemes(self):
        """Gets the child objects which have short tag of `ComponentLexemes`, long tag of `ComponentLexemes`"""
        return get_child_object(self.el, "ComponentLexemes", self.tag_dict)

    def HideMinorEntry(self):
        """Gets the child objects which have short tag of `HideMinorEntry`, long tag of `HideMinorEntry`"""
        return get_child_object(self.el, "HideMinorEntry", self.tag_dict)

    def PrimaryLexemes(self):
        """Gets the child objects which have short tag of `PrimaryLexemes`, long tag of `PrimaryLexemes`"""
        return get_child_object(self.el, "PrimaryLexemes", self.tag_dict)

    def RefType(self):
        """Gets the child objects which have short tag of `RefType`, long tag of `RefType`"""
        return get_child_object(self.el, "RefType", self.tag_dict)

    def ShowComplexFormsIn(self):
        """Gets the child objects which have short tag of `ShowComplexFormsIn`, long tag of `ShowComplexFormsIn`"""
        return get_child_object(self.el, "ShowComplexFormsIn", self.tag_dict)

    def VariantEntryTypes(self):
        """Gets the child objects which have short tag of `VariantEntryTypes`, long tag of `VariantEntryTypes`"""
        return get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
