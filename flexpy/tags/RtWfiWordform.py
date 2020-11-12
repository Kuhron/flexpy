from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtWfiWordform(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Analyses(self):
        return get_child_object(self.el, "Analyses", self.tag_dict)

    def Checksum(self):
        return get_child_object(self.el, "Checksum", self.tag_dict)

    def Form(self):
        return get_child_object(self.el, "Form", self.tag_dict)

    def SpellingStatus(self):
        return get_child_object(self.el, "SpellingStatus", self.tag_dict)
