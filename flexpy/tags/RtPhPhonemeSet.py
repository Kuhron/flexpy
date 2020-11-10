from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPhPhonemeSet(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.BoundaryMarkers = get_child_object(self.rt, "BoundaryMarkers", self.tag_dict)
        self.Description = get_child_object(self.rt, "Description", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.Phonemes = get_child_object(self.rt, "Phonemes", self.tag_dict)
