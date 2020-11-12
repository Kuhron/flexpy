from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexDb(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.ComplexEntryTypes = get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.DialectLabels = get_child_object(self.el, "DialectLabels", self.tag_dict)
        self.DomainTypes = get_child_object(self.el, "DomainTypes", self.tag_dict)
        self.ExtendedNoteTypes = get_child_object(self.el, "ExtendedNoteTypes", self.tag_dict)
        self.Introduction = get_child_object(self.el, "Introduction", self.tag_dict)
        self.IsBodyInSeparateSubentry = get_child_object(self.el, "IsBodyInSeparateSubentry", self.tag_dict)
        self.IsHeadwordCitationForm = get_child_object(self.el, "IsHeadwordCitationForm", self.tag_dict)
        self.Languages = get_child_object(self.el, "Languages", self.tag_dict)
        self.MorphTypes = get_child_object(self.el, "MorphTypes", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.PublicationTypes = get_child_object(self.el, "PublicationTypes", self.tag_dict)
        self.References = get_child_object(self.el, "References", self.tag_dict)
        self.Resources = get_child_object(self.el, "Resources", self.tag_dict)
        self.ReversalIndexes = get_child_object(self.el, "ReversalIndexes", self.tag_dict)
        self.SenseTypes = get_child_object(self.el, "SenseTypes", self.tag_dict)
        self.UsageTypes = get_child_object(self.el, "UsageTypes", self.tag_dict)
        self.VariantEntryTypes = get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
