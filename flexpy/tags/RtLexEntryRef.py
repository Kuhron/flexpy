from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntryRef(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.ComponentLexemes = get_child_object(self.rt, "ComponentLexemes", self.tag_dict)
        self.HideMinorEntry = get_child_object(self.rt, "HideMinorEntry", self.tag_dict)
        self.RefType = get_child_object(self.rt, "RefType", self.tag_dict)
        self.VariantEntryTypes = get_child_object(self.rt, "VariantEntryTypes", self.tag_dict)
