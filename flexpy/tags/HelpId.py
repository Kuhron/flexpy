from flexpy.FlexPyUtil import get_child_object

class HelpId:
    def __init__(self, el, tag_dict):
        self.el = el
        self.Uni = get_child_object(self.el, "Uni", self.tag_dict)
