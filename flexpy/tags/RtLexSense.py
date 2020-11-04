from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexSense(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Gloss = get_child_object(self.rt, "Gloss", self.rt_dict)
        self.MorphoSyntaxAnalysis = get_child_object(self.rt, "MorphoSyntaxAnalysis", self.rt_dict)
