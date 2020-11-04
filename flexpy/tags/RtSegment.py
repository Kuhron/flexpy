from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtSegment(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.Analyses = get_child_object(self.rt, "Analyses", self.rt_dict)
        self.BeginOffset = get_child_object(self.rt, "BeginOffset", self.rt_dict)
        self.BeginTimeOffset = get_child_object(self.rt, "BeginTimeOffset", self.rt_dict)
        self.EndTimeOffset = get_child_object(self.rt, "EndTimeOffset", self.rt_dict)
        self.FreeTranslation = get_child_object(self.rt, "FreeTranslation", self.rt_dict)
        self.MediaURI = get_child_object(self.rt, "MediaURI", self.rt_dict)
