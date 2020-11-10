from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtWfiMorphBundle(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.Form = get_child_object(self.el, "Form", self.tag_dict)
        self.Morph = get_child_object(self.el, "Morph", self.tag_dict)
        self.Msa = get_child_object(self.el, "Msa", self.tag_dict)
        self.Sense = get_child_object(self.el, "Sense", self.tag_dict)
