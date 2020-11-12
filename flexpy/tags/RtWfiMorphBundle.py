from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtWfiMorphBundle(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Form(self):
        return get_child_object(self.el, "Form", self.tag_dict)

    def Morph(self):
        return get_child_object(self.el, "Morph", self.tag_dict)

    def Msa(self):
        return get_child_object(self.el, "Msa", self.tag_dict)

    def Sense(self):
        return get_child_object(self.el, "Sense", self.tag_dict)
