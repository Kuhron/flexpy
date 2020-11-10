from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtMoStemAllomorph(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Form = get_child_object(self.rt, "Form", self.tag_dict)
        self.IsAbstract = get_child_object(self.rt, "IsAbstract", self.tag_dict)
        self.MorphType = get_child_object(self.rt, "MorphType", self.tag_dict)
