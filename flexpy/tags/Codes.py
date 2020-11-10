from flexpy.FlexPyUtil import get_child_object

class Codes:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtPhCode = get_child_object(self.el, "rt", self.tag_dict, class_name="PhCode")
