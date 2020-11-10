from flexpy.FlexPyUtil import get_child_object

class PromptText:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.Uni = get_child_object(self.el, "Uni", self.tag_dict)
