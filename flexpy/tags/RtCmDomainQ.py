from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmDomainQ(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.ExampleSentences = get_child_object(self.el, "ExampleSentences", self.tag_dict)
        self.ExampleWords = get_child_object(self.el, "ExampleWords", self.tag_dict)
        self.Question = get_child_object(self.el, "Question", self.tag_dict)
