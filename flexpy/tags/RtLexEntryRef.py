from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntryRef(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.ComponentLexemes = get_child_object(self.rt, "ComponentLexemes", self.rt_dict)
        self.HideMinorEntry = get_child_object(self.rt, "HideMinorEntry", self.rt_dict)
        self.RefType = get_child_object(self.rt, "RefType", self.rt_dict)
        self.VariantEntryTypes = get_child_object(self.rt, "VariantEntryTypes", self.rt_dict)
