from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Msa:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.RtMoDerivAffMsa = get_child_object(self.el, "rt", self.tag_dict, class_name="MoDerivAffMsa")
        self.RtMoInflAffMsa = get_child_object(self.el, "rt", self.tag_dict, class_name="MoInflAffMsa")
        self.RtMoStemMsa = get_child_object(self.el, "rt", self.tag_dict, class_name="MoStemMsa")
        self.RtMoUnclassifiedAffixMsa = get_child_object(self.el, "rt", self.tag_dict, class_name="MoUnclassifiedAffixMsa")
