from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtSegment(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.Analyses = get_child_object(self.rt, "Analyses", self.tag_dict)
        self.BeginOffset = get_child_object(self.rt, "BeginOffset", self.tag_dict)
        self.BeginTimeOffset = get_child_object(self.rt, "BeginTimeOffset", self.tag_dict)
        self.EndTimeOffset = get_child_object(self.rt, "EndTimeOffset", self.tag_dict)
        self.FreeTranslation = get_child_object(self.rt, "FreeTranslation", self.tag_dict)
        self.MediaURI = get_child_object(self.rt, "MediaURI", self.tag_dict)
