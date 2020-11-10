from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScrBookRef(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.BookAbbrev = get_child_object(self.rt, "BookAbbrev", self.tag_dict)
        self.BookName = get_child_object(self.rt, "BookName", self.tag_dict)
