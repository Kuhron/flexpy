from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmMediaContainer(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.MediaURIs = get_child_object(self.rt, "MediaURIs", self.tag_dict)
