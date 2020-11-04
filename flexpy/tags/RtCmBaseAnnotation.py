from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmBaseAnnotation(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.AnnotationType = get_child_object(self.rt, "AnnotationType", self.rt_dict)
        self.BeginObject = get_child_object(self.rt, "BeginObject", self.rt_dict)
        self.BeginOffset = get_child_object(self.rt, "BeginOffset", self.rt_dict)
        self.BeginRef = get_child_object(self.rt, "BeginRef", self.rt_dict)
        self.CompDetails = get_child_object(self.rt, "CompDetails", self.rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.EndObject = get_child_object(self.rt, "EndObject", self.rt_dict)
        self.EndOffset = get_child_object(self.rt, "EndOffset", self.rt_dict)
        self.EndRef = get_child_object(self.rt, "EndRef", self.rt_dict)
        self.Flid = get_child_object(self.rt, "Flid", self.rt_dict)
        self.WsSelector = get_child_object(self.rt, "WsSelector", self.rt_dict)
