from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtDsConstChart(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.BasedOn = get_child_object(self.rt, "BasedOn", self.tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.Template = get_child_object(self.rt, "Template", self.tag_dict)
