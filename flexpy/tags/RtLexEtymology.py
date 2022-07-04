from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEtymology(Rt):
    """A class for FLEx XML elements with the tag rt

    :param el: the `xml.etree.ElementTree.Element` object
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, parent_el=None, tag_dict=None):
        super().__init__(el, parent_el=parent_el, tag_dict=tag_dict)
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Comment(self):
        """Gets the child objects which have short tag of `Comment`, long tag of `Comment`"""
        return get_child_object(self.el, "Comment", self.tag_dict)

    def Form(self):
        """Gets the child objects which have short tag of `Form`, long tag of `Form`"""
        return get_child_object(self.el, "Form", self.tag_dict)

    def Gloss(self):
        """Gets the child objects which have short tag of `Gloss`, long tag of `Gloss`"""
        return get_child_object(self.el, "Gloss", self.tag_dict)

    def LanguageNotes(self):
        """Gets the child objects which have short tag of `LanguageNotes`, long tag of `LanguageNotes`"""
        return get_child_object(self.el, "LanguageNotes", self.tag_dict)

    def Source(self):
        """Gets the child objects which have short tag of `Source`, long tag of `Source`"""
        return get_child_object(self.el, "Source", self.tag_dict)
