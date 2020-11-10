from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhPhonData(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.NaturalClasses = get_child_object(self.rt, "NaturalClasses", self.tag_dict)
        self.PhonemeSets = get_child_object(self.rt, "PhonemeSets", self.tag_dict)
        self.PhonRuleFeats = get_child_object(self.rt, "PhonRuleFeats", self.tag_dict)
