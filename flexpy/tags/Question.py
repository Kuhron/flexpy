from flexpy.FlexPyUtil import get_child_object

class Question:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.AUni = get_child_object(self.el, "AUni", self.tag_dict)
