from flexpy.FlexPyUtil import get_child_object

class AStr:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.ws = self.el.attrib.get("ws")
        self.Run = get_child_object(self.el, "Run", self.tag_dict)
