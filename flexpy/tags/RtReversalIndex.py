from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtReversalIndex(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.PartsOfSpeech = get_child_object(self.el, "PartsOfSpeech", self.tag_dict)
        self.WritingSystem = get_child_object(self.el, "WritingSystem", self.tag_dict)
