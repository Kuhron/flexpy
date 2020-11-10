from flexpy.FlexPyUtil import get_child_object

class ExampleSentences:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.AStr = get_child_object(self.el, "AStr", self.tag_dict)
