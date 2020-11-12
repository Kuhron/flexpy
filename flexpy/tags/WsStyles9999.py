from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class WsStyles9999:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.WsProp = get_child_object(self.el, "WsProp", self.tag_dict)
