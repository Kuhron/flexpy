from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtSegment(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Analyses(self):
        return get_child_object(self.el, "Analyses", self.tag_dict)

    def BeginOffset(self):
        return get_child_object(self.el, "BeginOffset", self.tag_dict)

    def BeginTimeOffset(self):
        return get_child_object(self.el, "BeginTimeOffset", self.tag_dict)

    def EndTimeOffset(self):
        return get_child_object(self.el, "EndTimeOffset", self.tag_dict)

    def FreeTranslation(self):
        return get_child_object(self.el, "FreeTranslation", self.tag_dict)

    def MediaURI(self):
        return get_child_object(self.el, "MediaURI", self.tag_dict)

    def Notes(self):
        return get_child_object(self.el, "Notes", self.tag_dict)
