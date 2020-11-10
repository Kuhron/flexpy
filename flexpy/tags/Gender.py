from flexpy.FlexPyUtil import get_child_object

class Gender:
    def __init__(self, el, tag_dict):
        self.el = el
        self.val = self.el.attrib.get(val)
