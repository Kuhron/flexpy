from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtDsConstChart(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.BasedOn = get_child_object(self.el, "BasedOn", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Template = get_child_object(self.el, "Template", self.tag_dict)
