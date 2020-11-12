from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmDomainQ(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def ExampleSentences(self):
        return get_child_object(self.el, "ExampleSentences", self.tag_dict)

    def ExampleWords(self):
        return get_child_object(self.el, "ExampleWords", self.tag_dict)

    def Question(self):
        return get_child_object(self.el, "Question", self.tag_dict)
