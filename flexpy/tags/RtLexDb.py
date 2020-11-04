from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexDb(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.ComplexEntryTypes = get_child_object(self.rt, "ComplexEntryTypes", self.rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.DialectLabels = get_child_object(self.rt, "DialectLabels", self.rt_dict)
        self.DomainTypes = get_child_object(self.rt, "DomainTypes", self.rt_dict)
        self.ExtendedNoteTypes = get_child_object(self.rt, "ExtendedNoteTypes", self.rt_dict)
        self.Introduction = get_child_object(self.rt, "Introduction", self.rt_dict)
        self.IsBodyInSeparateSubentry = get_child_object(self.rt, "IsBodyInSeparateSubentry", self.rt_dict)
        self.IsHeadwordCitationForm = get_child_object(self.rt, "IsHeadwordCitationForm", self.rt_dict)
        self.Languages = get_child_object(self.rt, "Languages", self.rt_dict)
        self.MorphTypes = get_child_object(self.rt, "MorphTypes", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.PublicationTypes = get_child_object(self.rt, "PublicationTypes", self.rt_dict)
        self.References = get_child_object(self.rt, "References", self.rt_dict)
        self.Resources = get_child_object(self.rt, "Resources", self.rt_dict)
        self.ReversalIndexes = get_child_object(self.rt, "ReversalIndexes", self.rt_dict)
        self.SenseTypes = get_child_object(self.rt, "SenseTypes", self.rt_dict)
        self.UsageTypes = get_child_object(self.rt, "UsageTypes", self.rt_dict)
        self.VariantEntryTypes = get_child_object(self.rt, "VariantEntryTypes", self.rt_dict)
