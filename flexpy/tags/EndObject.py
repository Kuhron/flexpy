from flexpy.FlexPyUtil import get_child_object

class EndObject:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.RtStTxtPara = get_child_object(self.el, "rt", self.tag_dict, class_name="StTxtPara")