from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmMediaURI(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.MediaURI = get_child_object(self.rt, "MediaURI", self.rt_dict)
