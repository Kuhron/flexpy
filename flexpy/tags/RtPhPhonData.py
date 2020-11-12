from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtPhPhonData(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.NaturalClasses = get_child_object(self.el, "NaturalClasses", self.tag_dict)
        self.PhonRuleFeats = get_child_object(self.el, "PhonRuleFeats", self.tag_dict)
        self.PhonemeSets = get_child_object(self.el, "PhonemeSets", self.tag_dict)
