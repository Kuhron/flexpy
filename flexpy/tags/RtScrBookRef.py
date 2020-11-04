from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScrBookRef(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.BookAbbrev = get_child_object(self.rt, "BookAbbrev", self.rt_dict)
        self.BookName = get_child_object(self.rt, "BookName", self.rt_dict)
