from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class WsProp:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.fontFamily = self.el.attrib.get("fontFamily")
        self.fontsize = self.el.attrib.get("fontsize")
        self.fontsizeUnit = self.el.attrib.get("fontsizeUnit")
        self.ws = self.el.attrib.get("ws")

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)
