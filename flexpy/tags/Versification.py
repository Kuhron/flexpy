from flexpy.FlexPyUtil import get_child_object

class Versification:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.val = self.el.attrib.get("val")
