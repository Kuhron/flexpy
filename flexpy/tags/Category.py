from flexpy.FlexPyUtil import get_child_object

class Category:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtPartOfSpeech = get_child_object(self.el, "rt", self.tag_dict, class_name="PartOfSpeech")
