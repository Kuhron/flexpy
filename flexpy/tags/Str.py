from flexpy.FlexPyUtil import get_child_object

class Str:
    def __init__(self, el, tag_dict):
        self.el = el
        self.Run = get_child_object(self.el, "Run", self.tag_dict)
