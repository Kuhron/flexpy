from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexSense(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Definition(self):
        return get_child_object(self.el, "Definition", self.tag_dict)

    def Gloss(self):
        return get_child_object(self.el, "Gloss", self.tag_dict)

    def MorphoSyntaxAnalysis(self):
        return get_child_object(self.el, "MorphoSyntaxAnalysis", self.tag_dict)

    def ScientificName(self):
        return get_child_object(self.el, "ScientificName", self.tag_dict)

    def Source(self):
        return get_child_object(self.el, "Source", self.tag_dict)
