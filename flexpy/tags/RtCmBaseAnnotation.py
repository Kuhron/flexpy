from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmBaseAnnotation(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.AnnotationType = get_child_object(self.el, "AnnotationType", self.tag_dict)
        self.BeginObject = get_child_object(self.el, "BeginObject", self.tag_dict)
        self.BeginOffset = get_child_object(self.el, "BeginOffset", self.tag_dict)
        self.BeginRef = get_child_object(self.el, "BeginRef", self.tag_dict)
        self.CompDetails = get_child_object(self.el, "CompDetails", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.EndObject = get_child_object(self.el, "EndObject", self.tag_dict)
        self.EndOffset = get_child_object(self.el, "EndOffset", self.tag_dict)
        self.EndRef = get_child_object(self.el, "EndRef", self.tag_dict)
        self.Flid = get_child_object(self.el, "Flid", self.tag_dict)
        self.WsSelector = get_child_object(self.el, "WsSelector", self.tag_dict)
