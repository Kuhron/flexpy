from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtReversalIndex(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.Name = get_child_object(self.rt, "Name", self.tag_dict)
        self.PartsOfSpeech = get_child_object(self.rt, "PartsOfSpeech", self.tag_dict)
        self.WritingSystem = get_child_object(self.rt, "WritingSystem", self.tag_dict)
