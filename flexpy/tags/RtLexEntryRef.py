from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntryRef(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.ComplexEntryTypes = get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)
        self.ComponentLexemes = get_child_object(self.el, "ComponentLexemes", self.tag_dict)
        self.HideMinorEntry = get_child_object(self.el, "HideMinorEntry", self.tag_dict)
        self.PrimaryLexemes = get_child_object(self.el, "PrimaryLexemes", self.tag_dict)
        self.RefType = get_child_object(self.el, "RefType", self.tag_dict)
        self.ShowComplexFormsIn = get_child_object(self.el, "ShowComplexFormsIn", self.tag_dict)
        self.VariantEntryTypes = get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
