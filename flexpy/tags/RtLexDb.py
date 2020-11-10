from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexDb(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.ComplexEntryTypes = get_child_object(self.rt, "ComplexEntryTypes", self.tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.DialectLabels = get_child_object(self.rt, "DialectLabels", self.tag_dict)
        self.DomainTypes = get_child_object(self.rt, "DomainTypes", self.tag_dict)
        self.ExtendedNoteTypes = get_child_object(self.rt, "ExtendedNoteTypes", self.tag_dict)
        self.Introduction = get_child_object(self.rt, "Introduction", self.tag_dict)
        self.IsBodyInSeparateSubentry = get_child_object(self.rt, "IsBodyInSeparateSubentry", self.tag_dict)
        self.IsHeadwordCitationForm = get_child_object(self.rt, "IsHeadwordCitationForm", self.tag_dict)
        self.Languages = get_child_object(self.rt, "Languages", self.tag_dict)
        self.MorphTypes = get_child_object(self.rt, "MorphTypes", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.PublicationTypes = get_child_object(self.rt, "PublicationTypes", self.tag_dict)
        self.References = get_child_object(self.rt, "References", self.tag_dict)
        self.Resources = get_child_object(self.rt, "Resources", self.tag_dict)
        self.ReversalIndexes = get_child_object(self.rt, "ReversalIndexes", self.tag_dict)
        self.SenseTypes = get_child_object(self.rt, "SenseTypes", self.tag_dict)
        self.UsageTypes = get_child_object(self.rt, "UsageTypes", self.tag_dict)
        self.VariantEntryTypes = get_child_object(self.rt, "VariantEntryTypes", self.tag_dict)
