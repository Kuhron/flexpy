from flexpy.FlexPyUtil import get_child_object

class Introduction:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtStText = get_child_object(self.el, "rt", self.tag_dict, class_name="StText")
