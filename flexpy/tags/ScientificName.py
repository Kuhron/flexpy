from flexpy.FlexPyUtil import get_child_object

class ScientificName:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.Str = get_child_object(self.el, "Str", self.tag_dict)