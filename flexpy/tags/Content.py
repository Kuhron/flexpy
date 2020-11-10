from flexpy.FlexPyUtil import get_child_object

class Content:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.AStr = get_child_object(self.el, "AStr", self.tag_dict)
