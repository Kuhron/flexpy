from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoInflAffixTemplate(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Disabled(self):
        return get_child_object(self.el, "Disabled", self.tag_dict)

    def Final(self):
        return get_child_object(self.el, "Final", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def PrefixSlots(self):
        return get_child_object(self.el, "PrefixSlots", self.tag_dict)

    def SuffixSlots(self):
        return get_child_object(self.el, "SuffixSlots", self.tag_dict)
