from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmDomainQ(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.ExampleWords = get_child_object(self.rt, "ExampleWords", self.tag_dict)
        self.Question = get_child_object(self.rt, "Question", self.tag_dict)
