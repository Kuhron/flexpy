from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmAgent(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.Approves = get_child_object(self.el, "Approves", self.tag_dict)
        self.Disapproves = get_child_object(self.el, "Disapproves", self.tag_dict)
        self.Human = get_child_object(self.el, "Human", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.Notes = get_child_object(self.el, "Notes", self.tag_dict)
        self.Version = get_child_object(self.el, "Version", self.tag_dict)
