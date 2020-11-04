from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtLexPronunciation(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Form = get_child_object(self.rt, "Form", self.rt_dict)
