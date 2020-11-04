from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtDsConstChart(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.BasedOn = get_child_object(self.rt, "BasedOn", self.rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.Template = get_child_object(self.rt, "Template", self.rt_dict)
