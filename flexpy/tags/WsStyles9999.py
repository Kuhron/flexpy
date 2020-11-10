from flexpy.FlexPyUtil import get_child_object

class WsStyles9999:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.WsProp = get_child_object(self.el, "WsProp", self.tag_dict)
