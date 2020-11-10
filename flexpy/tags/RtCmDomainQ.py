from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmDomainQ(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.ExampleSentences = get_child_object(self.el, "ExampleSentences", self.tag_dict)
        self.ExampleWords = get_child_object(self.el, "ExampleWords", self.tag_dict)
        self.Question = get_child_object(self.el, "Question", self.tag_dict)
