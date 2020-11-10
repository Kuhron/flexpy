from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtNote(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Content = get_child_object(self.rt, "Content", self.tag_dict)
