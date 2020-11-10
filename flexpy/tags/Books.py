from flexpy.FlexPyUtil import get_child_object

class Books:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtScrBookRef = get_child_object(self.el, "rt", self.tag_dict, class_name="ScrBookRef")
