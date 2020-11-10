from flexpy.FlexPyUtil import get_child_object

class Description:
    def __init__(self, el, tag_dict):
        self.el = el
        self.AStr = get_child_object(self.el, "AStr", self.tag_dict)
