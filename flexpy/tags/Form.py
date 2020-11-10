from flexpy.FlexPyUtil import get_child_object

class Form:
    def __init__(self, el, tag_dict):
        self.el = el
        self.AStr = get_child_object(self.el, "AStr", self.tag_dict)
        self.AUni = get_child_object(self.el, "AUni", self.tag_dict)
        self.Str = get_child_object(self.el, "Str", self.tag_dict)
