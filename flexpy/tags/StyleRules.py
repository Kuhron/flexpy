from flexpy.FlexPyUtil import get_child_object

class StyleRules:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.Prop = get_child_object(self.el, "Prop", self.tag_dict)