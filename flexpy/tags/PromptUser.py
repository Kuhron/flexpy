from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class PromptUser:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.val = self.el.attrib.get("val")
        self.child_objects = get_ordered_child_objects(el, tag_dict)
