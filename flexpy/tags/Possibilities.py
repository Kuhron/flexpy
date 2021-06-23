from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Possibilities:
    """A class for FLEx XML elements with the tag Possibilities
    :param el: the `xml.etree.ElementTree.Element object`
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.fp = self.el.attrib.get("fp")

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def RtCmAnnotationDefn(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtCmAnnotationDefn`, class name of `CmAnnotationDefn`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="CmAnnotationDefn")

    def RtCmAnthroItem(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtCmAnthroItem`, class name of `CmAnthroItem`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="CmAnthroItem")

    def RtCmPerson(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtCmPerson`, class name of `CmPerson`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="CmPerson")

    def RtCmPossibility(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtCmPossibility`, class name of `CmPossibility`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="CmPossibility")

    def RtCmSemanticDomain(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtCmSemanticDomain`, class name of `CmSemanticDomain`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="CmSemanticDomain")

    def RtLexEntryInflType(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtLexEntryInflType`, class name of `LexEntryInflType`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryInflType")

    def RtLexEntryType(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtLexEntryType`, class name of `LexEntryType`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryType")

    def RtLexRefType(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtLexRefType`, class name of `LexRefType`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="LexRefType")

    def RtMoMorphType(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtMoMorphType`, class name of `MoMorphType`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="MoMorphType")

    def RtPartOfSpeech(self):
        """Gets the child objects which have short tag of `rt`, long tag of `RtPartOfSpeech`, class name of `PartOfSpeech`"""
        return get_child_object(self.el, "rt", self.tag_dict, class_name="PartOfSpeech")
