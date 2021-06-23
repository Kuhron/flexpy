from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Column:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.fp = self.el.attrib.get("fp")

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def RtCmPossibility(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="CmPossibility")
