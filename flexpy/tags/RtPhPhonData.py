from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtPhPhonData(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def NaturalClasses(self):
        return get_child_object(self.el, "NaturalClasses", self.tag_dict)

    def PhonRuleFeats(self):
        return get_child_object(self.el, "PhonRuleFeats", self.tag_dict)

    def PhonemeSets(self):
        return get_child_object(self.el, "PhonemeSets", self.tag_dict)
