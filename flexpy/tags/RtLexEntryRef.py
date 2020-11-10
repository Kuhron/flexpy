from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntryRef(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.ComplexEntryTypes = get_child_object(self.el, "ComplexEntryTypes", self.tag_dict)
        self.ComponentLexemes = get_child_object(self.el, "ComponentLexemes", self.tag_dict)
        self.HideMinorEntry = get_child_object(self.el, "HideMinorEntry", self.tag_dict)
        self.PrimaryLexemes = get_child_object(self.el, "PrimaryLexemes", self.tag_dict)
        self.RefType = get_child_object(self.el, "RefType", self.tag_dict)
        self.ShowComplexFormsIn = get_child_object(self.el, "ShowComplexFormsIn", self.tag_dict)
        self.VariantEntryTypes = get_child_object(self.el, "VariantEntryTypes", self.tag_dict)
