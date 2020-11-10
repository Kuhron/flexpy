from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScrBookRef(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.BookAbbrev = get_child_object(self.el, "BookAbbrev", self.tag_dict)
        self.BookName = get_child_object(self.el, "BookName", self.tag_dict)
        self.BookNameAlt = get_child_object(self.el, "BookNameAlt", self.tag_dict)
