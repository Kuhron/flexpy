from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScrRefSystem(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Books = get_child_object(self.rt, "Books", self.tag_dict)
