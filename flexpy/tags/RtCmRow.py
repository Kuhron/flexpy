from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmRow(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.Cells = get_child_object(self.el, "Cells", self.tag_dict)
