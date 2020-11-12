from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoAffixAllomorph(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.Form = get_child_object(self.el, "Form", self.tag_dict)
        self.IsAbstract = get_child_object(self.el, "IsAbstract", self.tag_dict)
        self.MorphType = get_child_object(self.el, "MorphType", self.tag_dict)
