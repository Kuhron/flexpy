from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhBdryMarker(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.Codes = get_child_object(self.el, "Codes", self.tag_dict)
        self.Description = get_child_object(self.el, "Description", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)