from flexpy.FlexPyUtil import get_child_object

class Rows:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtCmRow = get_child_object(self.el, "rt", self.tag_dict, class_name="CmRow")
