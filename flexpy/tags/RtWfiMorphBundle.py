from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtWfiMorphBundle(Rt):
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

    def Form(self):
        """Gets the child objects which have short tag of `Form`, long tag of `Form`"""
        return get_child_object(self.el, "Form", self.tag_dict)

    def InflType(self):
        """Gets the child objects which have short tag of `InflType`, long tag of `InflType`"""
        return get_child_object(self.el, "InflType", self.tag_dict)

    def Morph(self):
        """Gets the child objects which have short tag of `Morph`, long tag of `Morph`"""
        return get_child_object(self.el, "Morph", self.tag_dict)

    def Msa(self):
        """Gets the child objects which have short tag of `Msa`, long tag of `Msa`"""
        return get_child_object(self.el, "Msa", self.tag_dict)

    def Sense(self):
        """Gets the child objects which have short tag of `Sense`, long tag of `Sense`"""
        return get_child_object(self.el, "Sense", self.tag_dict)
