from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexSense(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Gloss = get_child_object(self.rt, "Gloss", self.tag_dict)
        self.MorphoSyntaxAnalysis = get_child_object(self.rt, "MorphoSyntaxAnalysis", self.tag_dict)
