from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPunctuationForm(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Form = get_child_object(self.rt, "Form", self.tag_dict)
