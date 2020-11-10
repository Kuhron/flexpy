from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmBaseAnnotation(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.AnnotationType = get_child_object(self.rt, "AnnotationType", self.tag_dict)
        self.BeginObject = get_child_object(self.rt, "BeginObject", self.tag_dict)
        self.BeginOffset = get_child_object(self.rt, "BeginOffset", self.tag_dict)
        self.BeginRef = get_child_object(self.rt, "BeginRef", self.tag_dict)
        self.CompDetails = get_child_object(self.rt, "CompDetails", self.tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.EndObject = get_child_object(self.rt, "EndObject", self.tag_dict)
        self.EndOffset = get_child_object(self.rt, "EndOffset", self.tag_dict)
        self.EndRef = get_child_object(self.rt, "EndRef", self.tag_dict)
        self.Flid = get_child_object(self.rt, "Flid", self.tag_dict)
        self.WsSelector = get_child_object(self.rt, "WsSelector", self.tag_dict)
