from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoMorphData(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def ParserParameters(self):
        return get_child_object(self.el, "ParserParameters", self.tag_dict)

    def ProdRestrict(self):
        return get_child_object(self.el, "ProdRestrict", self.tag_dict)
