from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiAnalysis(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.Category = get_child_object(self.el, "Category", self.tag_dict)
        self.Evaluations = get_child_object(self.el, "Evaluations", self.tag_dict)
        self.Meanings = get_child_object(self.el, "Meanings", self.tag_dict)
        self.MorphBundles = get_child_object(self.el, "MorphBundles", self.tag_dict)
