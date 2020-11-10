from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntry(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.AlternateForms = get_child_object(self.el, "AlternateForms", self.tag_dict)
        self.Comment = get_child_object(self.el, "Comment", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.DoNotPublishIn = get_child_object(self.el, "DoNotPublishIn", self.tag_dict)
        self.DoNotUseForParsing = get_child_object(self.el, "DoNotUseForParsing", self.tag_dict)
        self.EntryRefs = get_child_object(self.el, "EntryRefs", self.tag_dict)
        self.HomographNumber = get_child_object(self.el, "HomographNumber", self.tag_dict)
        self.LexemeForm = get_child_object(self.el, "LexemeForm", self.tag_dict)
        self.MorphoSyntaxAnalyses = get_child_object(self.el, "MorphoSyntaxAnalyses", self.tag_dict)
        self.Pronunciations = get_child_object(self.el, "Pronunciations", self.tag_dict)
        self.Senses = get_child_object(self.el, "Senses", self.tag_dict)
