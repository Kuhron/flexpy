from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmBaseAnnotation(Rt):
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

    def AnnotationType(self):
        """Gets the child objects which have short tag of `AnnotationType`, long tag of `AnnotationType`"""
        return get_child_object(self.el, "AnnotationType", self.tag_dict)

    def BeginObject(self):
        """Gets the child objects which have short tag of `BeginObject`, long tag of `BeginObject`"""
        return get_child_object(self.el, "BeginObject", self.tag_dict)

    def BeginOffset(self):
        """Gets the child objects which have short tag of `BeginOffset`, long tag of `BeginOffset`"""
        return get_child_object(self.el, "BeginOffset", self.tag_dict)

    def BeginRef(self):
        """Gets the child objects which have short tag of `BeginRef`, long tag of `BeginRef`"""
        return get_child_object(self.el, "BeginRef", self.tag_dict)

    def CompDetails(self):
        """Gets the child objects which have short tag of `CompDetails`, long tag of `CompDetails`"""
        return get_child_object(self.el, "CompDetails", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def EndObject(self):
        """Gets the child objects which have short tag of `EndObject`, long tag of `EndObject`"""
        return get_child_object(self.el, "EndObject", self.tag_dict)

    def EndOffset(self):
        """Gets the child objects which have short tag of `EndOffset`, long tag of `EndOffset`"""
        return get_child_object(self.el, "EndOffset", self.tag_dict)

    def EndRef(self):
        """Gets the child objects which have short tag of `EndRef`, long tag of `EndRef`"""
        return get_child_object(self.el, "EndRef", self.tag_dict)

    def Flid(self):
        """Gets the child objects which have short tag of `Flid`, long tag of `Flid`"""
        return get_child_object(self.el, "Flid", self.tag_dict)

    def WsSelector(self):
        """Gets the child objects which have short tag of `WsSelector`, long tag of `WsSelector`"""
        return get_child_object(self.el, "WsSelector", self.tag_dict)
