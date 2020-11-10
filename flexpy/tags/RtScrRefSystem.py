from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScrRefSystem(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.Books = get_child_object(self.el, "Books", self.tag_dict)
