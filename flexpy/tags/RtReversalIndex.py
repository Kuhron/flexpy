from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtReversalIndex(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.Name = get_child_object(self.rt, "Name", self.rt_dict)
        self.PartsOfSpeech = get_child_object(self.rt, "PartsOfSpeech", self.rt_dict)
        self.WritingSystem = get_child_object(self.rt, "WritingSystem", self.rt_dict)
