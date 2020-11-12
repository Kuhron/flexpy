from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Context:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.val = self.el.attrib.get("val")

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)
