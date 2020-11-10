from flexpy.FlexPyUtil import get_child_object

class WsStyles9999:
    def __init__(self, el, tag_dict):
        self.el = el
        self.WsProp = get_child_object(self.el, "WsProp", self.tag_dict)
