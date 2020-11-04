from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhPhonData(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.NaturalClasses = get_child_object(self.rt, "NaturalClasses", self.rt_dict)
        self.PhonemeSets = get_child_object(self.rt, "PhonemeSets", self.rt_dict)
        self.PhonRuleFeats = get_child_object(self.rt, "PhonRuleFeats", self.rt_dict)
