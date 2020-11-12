from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntry(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def AlternateForms(self):
        return get_child_object(self.el, "AlternateForms", self.tag_dict)

    def Comment(self):
        return get_child_object(self.el, "Comment", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DoNotPublishIn(self):
        return get_child_object(self.el, "DoNotPublishIn", self.tag_dict)

    def DoNotUseForParsing(self):
        return get_child_object(self.el, "DoNotUseForParsing", self.tag_dict)

    def EntryRefs(self):
        return get_child_object(self.el, "EntryRefs", self.tag_dict)

    def HomographNumber(self):
        return get_child_object(self.el, "HomographNumber", self.tag_dict)

    def LexemeForm(self):
        return get_child_object(self.el, "LexemeForm", self.tag_dict)

    def MorphoSyntaxAnalyses(self):
        return get_child_object(self.el, "MorphoSyntaxAnalyses", self.tag_dict)

    def Pronunciations(self):
        return get_child_object(self.el, "Pronunciations", self.tag_dict)

    def Senses(self):
        return get_child_object(self.el, "Senses", self.tag_dict)
