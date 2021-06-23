from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoEndoCompound(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Description(self):
        return get_child_object(self.el, "Description", self.tag_dict)

    def Disabled(self):
        return get_child_object(self.el, "Disabled", self.tag_dict)

    def HeadLast(self):
        return get_child_object(self.el, "HeadLast", self.tag_dict)

    def LeftMsa(self):
        return get_child_object(self.el, "LeftMsa", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def OverridingMsa(self):
        return get_child_object(self.el, "OverridingMsa", self.tag_dict)

    def RightMsa(self):
        return get_child_object(self.el, "RightMsa", self.tag_dict)
