from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtScrBookRef(Rt):
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

    def BookAbbrev(self):
        """Gets the child objects which have short tag of `BookAbbrev`, long tag of `BookAbbrev`"""
        return get_child_object(self.el, "BookAbbrev", self.tag_dict)

    def BookName(self):
        """Gets the child objects which have short tag of `BookName`, long tag of `BookName`"""
        return get_child_object(self.el, "BookName", self.tag_dict)

    def BookNameAlt(self):
        """Gets the child objects which have short tag of `BookNameAlt`, long tag of `BookNameAlt`"""
        return get_child_object(self.el, "BookNameAlt", self.tag_dict)
