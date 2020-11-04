from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScrRefSystem(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Books = get_child_object(self.rt, "Books", self.rt_dict)
