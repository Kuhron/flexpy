from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexDb(Rt):
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

    def ComplexEntryTypes(self):
        """Gets the child objects which have short tag of `ComplexEntryTypes`, long tag of `ComplexEntryTypes`"""
        return get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DialectLabels(self):
        """Gets the child objects which have short tag of `DialectLabels`, long tag of `DialectLabels`"""
        return get_child_object(self.el, "DialectLabels", self.tag_dict)

    def DomainTypes(self):
        """Gets the child objects which have short tag of `DomainTypes`, long tag of `DomainTypes`"""
        return get_child_object(self.el, "DomainTypes", self.tag_dict)

    def ExtendedNoteTypes(self):
        """Gets the child objects which have short tag of `ExtendedNoteTypes`, long tag of `ExtendedNoteTypes`"""
        return get_child_object(self.el, "ExtendedNoteTypes", self.tag_dict)

    def IsBodyInSeparateSubentry(self):
        """Gets the child objects which have short tag of `IsBodyInSeparateSubentry`, long tag of `IsBodyInSeparateSubentry`"""
        return get_child_object(self.el, "IsBodyInSeparateSubentry", self.tag_dict)

    def IsHeadwordCitationForm(self):
        """Gets the child objects which have short tag of `IsHeadwordCitationForm`, long tag of `IsHeadwordCitationForm`"""
        return get_child_object(self.el, "IsHeadwordCitationForm", self.tag_dict)

    def Languages(self):
        """Gets the child objects which have short tag of `Languages`, long tag of `Languages`"""
        return get_child_object(self.el, "Languages", self.tag_dict)

    def MorphTypes(self):
        """Gets the child objects which have short tag of `MorphTypes`, long tag of `MorphTypes`"""
        return get_child_object(self.el, "MorphTypes", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def PublicationTypes(self):
        """Gets the child objects which have short tag of `PublicationTypes`, long tag of `PublicationTypes`"""
        return get_child_object(self.el, "PublicationTypes", self.tag_dict)

    def References(self):
        """Gets the child objects which have short tag of `References`, long tag of `References`"""
        return get_child_object(self.el, "References", self.tag_dict)

    def Resources(self):
        """Gets the child objects which have short tag of `Resources`, long tag of `Resources`"""
        return get_child_object(self.el, "Resources", self.tag_dict)

    def ReversalIndexes(self):
        """Gets the child objects which have short tag of `ReversalIndexes`, long tag of `ReversalIndexes`"""
        return get_child_object(self.el, "ReversalIndexes", self.tag_dict)

    def SenseTypes(self):
        """Gets the child objects which have short tag of `SenseTypes`, long tag of `SenseTypes`"""
        return get_child_object(self.el, "SenseTypes", self.tag_dict)

    def UsageTypes(self):
        """Gets the child objects which have short tag of `UsageTypes`, long tag of `UsageTypes`"""
        return get_child_object(self.el, "UsageTypes", self.tag_dict)

    def VariantEntryTypes(self):
        """Gets the child objects which have short tag of `VariantEntryTypes`, long tag of `VariantEntryTypes`"""
        return get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
