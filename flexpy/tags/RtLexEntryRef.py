from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntryRef(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def ComplexEntryTypes(self):
        return get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)

    def ComponentLexemes(self):
        return get_child_object(self.el, "ComponentLexemes", self.tag_dict)

    def HideMinorEntry(self):
        return get_child_object(self.el, "HideMinorEntry", self.tag_dict)

    def PrimaryLexemes(self):
        return get_child_object(self.el, "PrimaryLexemes", self.tag_dict)

    def RefType(self):
        return get_child_object(self.el, "RefType", self.tag_dict)

    def ShowComplexFormsIn(self):
        return get_child_object(self.el, "ShowComplexFormsIn", self.tag_dict)

    def VariantEntryTypes(self):
        return get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
