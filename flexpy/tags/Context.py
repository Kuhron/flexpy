from flexpy.FlexPyUtil import get_child_object

class Context:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.val = self.el.attrib.get("val")
