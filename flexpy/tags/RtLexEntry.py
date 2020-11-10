from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntry(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.DoNotUseForParsing = get_child_object(self.rt, "DoNotUseForParsing", self.tag_dict)
        self.HomographNumber = get_child_object(self.rt, "HomographNumber", self.tag_dict)
        self.LexemeForm = get_child_object(self.rt, "LexemeForm", self.tag_dict)
        self.MorphoSyntaxAnalyses = get_child_object(self.rt, "MorphoSyntaxAnalyses", self.tag_dict)
        self.Senses = get_child_object(self.rt, "Senses", self.tag_dict)
