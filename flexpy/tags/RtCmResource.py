from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmResource(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.Version = get_child_object(self.rt, "Version", self.tag_dict)
