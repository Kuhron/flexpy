from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtNote(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Content = get_child_object(self.rt, "Content", self.rt_dict)
