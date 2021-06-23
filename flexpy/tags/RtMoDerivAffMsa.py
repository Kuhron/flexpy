from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtMoDerivAffMsa(Rt):
    """A class for FLEx XML elements with the tag rt
    :param el: the `xml.etree.ElementTree.Element object`
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def FromPartOfSpeech(self):
        """Gets the child objects which have short tag of `FromPartOfSpeech`, long tag of `FromPartOfSpeech`"""
        return get_child_object(self.el, "FromPartOfSpeech", self.tag_dict)

    def ToPartOfSpeech(self):
        """Gets the child objects which have short tag of `ToPartOfSpeech`, long tag of `ToPartOfSpeech`"""
        return get_child_object(self.el, "ToPartOfSpeech", self.tag_dict)
