from flexpy.FlexPyUtil import get_child_object

class Contents:
    def __init__(self, el, tag_dict):
        self.el = el
        self.Str = get_child_object(self.el, "Str", self.tag_dict)
        self.RtStText = get_child_object(self.el, "rt", self.tag_dict, class_name="StText")
