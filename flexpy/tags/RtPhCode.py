from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhCode(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.Representation = get_child_object(self.el, "Representation", self.tag_dict)