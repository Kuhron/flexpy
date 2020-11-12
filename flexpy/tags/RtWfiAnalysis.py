from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtWfiAnalysis(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Category(self):
        return get_child_object(self.el, "Category", self.tag_dict)

    def Evaluations(self):
        return get_child_object(self.el, "Evaluations", self.tag_dict)

    def Meanings(self):
        return get_child_object(self.el, "Meanings", self.tag_dict)

    def MorphBundles(self):
        return get_child_object(self.el, "MorphBundles", self.tag_dict)
