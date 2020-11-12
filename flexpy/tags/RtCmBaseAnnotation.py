from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmBaseAnnotation(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def AnnotationType(self):
        return get_child_object(self.el, "AnnotationType", self.tag_dict)

    def BeginObject(self):
        return get_child_object(self.el, "BeginObject", self.tag_dict)

    def BeginOffset(self):
        return get_child_object(self.el, "BeginOffset", self.tag_dict)

    def BeginRef(self):
        return get_child_object(self.el, "BeginRef", self.tag_dict)

    def CompDetails(self):
        return get_child_object(self.el, "CompDetails", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def EndObject(self):
        return get_child_object(self.el, "EndObject", self.tag_dict)

    def EndOffset(self):
        return get_child_object(self.el, "EndOffset", self.tag_dict)

    def EndRef(self):
        return get_child_object(self.el, "EndRef", self.tag_dict)

    def Flid(self):
        return get_child_object(self.el, "Flid", self.tag_dict)

    def WsSelector(self):
        return get_child_object(self.el, "WsSelector", self.tag_dict)
