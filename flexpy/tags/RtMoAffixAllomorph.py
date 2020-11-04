from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtMoAffixAllomorph(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Form = get_child_object(self.rt, "Form", self.rt_dict)
        self.IsAbstract = get_child_object(self.rt, "IsAbstract", self.rt_dict)
        self.MorphType = get_child_object(self.rt, "MorphType", self.rt_dict)
