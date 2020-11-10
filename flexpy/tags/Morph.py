from flexpy.FlexPyUtil import get_child_object

class Morph:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtMoAffixAllomorph = get_child_object(self.el, "rt", self.tag_dict, class_name="MoAffixAllomorph")
        self.RtMoStemAllomorph = get_child_object(self.el, "rt", self.tag_dict, class_name="MoStemAllomorph")
