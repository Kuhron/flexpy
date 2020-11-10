from flexpy.FlexPyUtil import get_child_object

class SenseTypes:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.RtCmPossibilityList = get_child_object(self.el, "rt", self.tag_dict, class_name="CmPossibilityList")
