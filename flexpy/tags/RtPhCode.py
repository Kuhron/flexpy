from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhCode(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Representation = get_child_object(self.rt, "Representation", self.rt_dict)
