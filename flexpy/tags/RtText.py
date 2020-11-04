from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtText(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.IsTranslated = get_child_object(self.rt, "IsTranslated", self.rt_dict)
