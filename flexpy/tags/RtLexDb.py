from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexDb(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def ComplexEntryTypes(self):
        return get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DialectLabels(self):
        return get_child_object(self.el, "DialectLabels", self.tag_dict)

    def DomainTypes(self):
        return get_child_object(self.el, "DomainTypes", self.tag_dict)

    def ExtendedNoteTypes(self):
        return get_child_object(self.el, "ExtendedNoteTypes", self.tag_dict)

    def Introduction(self):
        return get_child_object(self.el, "Introduction", self.tag_dict)

    def IsBodyInSeparateSubentry(self):
        return get_child_object(self.el, "IsBodyInSeparateSubentry", self.tag_dict)

    def IsHeadwordCitationForm(self):
        return get_child_object(self.el, "IsHeadwordCitationForm", self.tag_dict)

    def Languages(self):
        return get_child_object(self.el, "Languages", self.tag_dict)

    def MorphTypes(self):
        return get_child_object(self.el, "MorphTypes", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def PublicationTypes(self):
        return get_child_object(self.el, "PublicationTypes", self.tag_dict)

    def References(self):
        return get_child_object(self.el, "References", self.tag_dict)

    def Resources(self):
        return get_child_object(self.el, "Resources", self.tag_dict)

    def ReversalIndexes(self):
        return get_child_object(self.el, "ReversalIndexes", self.tag_dict)

    def SenseTypes(self):
        return get_child_object(self.el, "SenseTypes", self.tag_dict)

    def UsageTypes(self):
        return get_child_object(self.el, "UsageTypes", self.tag_dict)

    def VariantEntryTypes(self):
        return get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
