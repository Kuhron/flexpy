from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexSense(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.Definition = get_child_object(self.el, "Definition", self.tag_dict)
        self.Gloss = get_child_object(self.el, "Gloss", self.tag_dict)
        self.MorphoSyntaxAnalysis = get_child_object(self.el, "MorphoSyntaxAnalysis", self.tag_dict)
        self.ScientificName = get_child_object(self.el, "ScientificName", self.tag_dict)
        self.Source = get_child_object(self.el, "Source", self.tag_dict)
