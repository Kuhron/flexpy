from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtPunctuationForm(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.Form = get_child_object(self.el, "Form", self.tag_dict)
