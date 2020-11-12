from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtStTxtPara(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.Contents = get_child_object(self.el, "Contents", self.tag_dict)
        self.ParseIsCurrent = get_child_object(self.el, "ParseIsCurrent", self.tag_dict)
        self.Segments = get_child_object(self.el, "Segments", self.tag_dict)
        self.StyleRules = get_child_object(self.el, "StyleRules", self.tag_dict)
