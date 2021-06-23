from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtSegment(Rt):
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

    def Analyses(self):
        """Gets the child objects which have short tag of `Analyses`, long tag of `Analyses`"""
        return get_child_object(self.el, "Analyses", self.tag_dict)

    def BeginOffset(self):
        """Gets the child objects which have short tag of `BeginOffset`, long tag of `BeginOffset`"""
        return get_child_object(self.el, "BeginOffset", self.tag_dict)

    def BeginTimeOffset(self):
        """Gets the child objects which have short tag of `BeginTimeOffset`, long tag of `BeginTimeOffset`"""
        return get_child_object(self.el, "BeginTimeOffset", self.tag_dict)

    def EndTimeOffset(self):
        """Gets the child objects which have short tag of `EndTimeOffset`, long tag of `EndTimeOffset`"""
        return get_child_object(self.el, "EndTimeOffset", self.tag_dict)

    def FreeTranslation(self):
        """Gets the child objects which have short tag of `FreeTranslation`, long tag of `FreeTranslation`"""
        return get_child_object(self.el, "FreeTranslation", self.tag_dict)

    def MediaURI(self):
        """Gets the child objects which have short tag of `MediaURI`, long tag of `MediaURI`"""
        return get_child_object(self.el, "MediaURI", self.tag_dict)

    def Notes(self):
        """Gets the child objects which have short tag of `Notes`, long tag of `Notes`"""
        return get_child_object(self.el, "Notes", self.tag_dict)
