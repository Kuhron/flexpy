from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiWordform(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.Analyses = get_child_object(self.el, "Analyses", self.tag_dict)
        self.Checksum = get_child_object(self.el, "Checksum", self.tag_dict)
        self.Form = get_child_object(self.el, "Form", self.tag_dict)
        self.SpellingStatus = get_child_object(self.el, "SpellingStatus", self.tag_dict)
