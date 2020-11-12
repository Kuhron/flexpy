from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Msa:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def RtMoDerivAffMsa(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="MoDerivAffMsa")

    def RtMoInflAffMsa(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="MoInflAffMsa")

    def RtMoStemMsa(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="MoStemMsa")

    def RtMoUnclassifiedAffixMsa(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="MoUnclassifiedAffixMsa")
