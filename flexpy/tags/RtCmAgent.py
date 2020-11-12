from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmAgent(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Approves(self):
        return get_child_object(self.el, "Approves", self.tag_dict)

    def Disapproves(self):
        return get_child_object(self.el, "Disapproves", self.tag_dict)

    def Human(self):
        return get_child_object(self.el, "Human", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def Notes(self):
        return get_child_object(self.el, "Notes", self.tag_dict)

    def Version(self):
        return get_child_object(self.el, "Version", self.tag_dict)
