from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtSegment(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.Analyses = get_child_object(self.el, "Analyses", self.tag_dict)
        self.BeginOffset = get_child_object(self.el, "BeginOffset", self.tag_dict)
        self.BeginTimeOffset = get_child_object(self.el, "BeginTimeOffset", self.tag_dict)
        self.EndTimeOffset = get_child_object(self.el, "EndTimeOffset", self.tag_dict)
        self.FreeTranslation = get_child_object(self.el, "FreeTranslation", self.tag_dict)
        self.MediaURI = get_child_object(self.el, "MediaURI", self.tag_dict)
        self.Notes = get_child_object(self.el, "Notes", self.tag_dict)
