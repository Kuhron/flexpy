from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexEntry(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.DoNotUseForParsing = get_child_object(self.rt, "DoNotUseForParsing", self.rt_dict)
        self.HomographNumber = get_child_object(self.rt, "HomographNumber", self.rt_dict)
        self.LexemeForm = get_child_object(self.rt, "LexemeForm", self.rt_dict)
        self.MorphoSyntaxAnalyses = get_child_object(self.rt, "MorphoSyntaxAnalyses", self.rt_dict)
        self.Senses = get_child_object(self.rt, "Senses", self.rt_dict)
