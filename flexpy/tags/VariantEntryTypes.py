from flexpy.FlexPyUtil import get_child_object

class VariantEntryTypes:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.RtCmPossibilityList = get_child_object(self.el, "rt", self.tag_dict, class_name="CmPossibilityList")
        self.RtLexEntryInflType = get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryInflType")
        self.RtLexEntryType = get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryType")
