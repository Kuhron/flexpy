from flexpy.FlexPyUtil import get_child_object

class Abbreviation:
    def __init__(self, el, tag_dict):
        self.el = el
        self.AUni = get_child_object(self.el, "AUni", self.tag_dict)
