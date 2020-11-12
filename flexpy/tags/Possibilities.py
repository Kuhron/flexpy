from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Possibilities:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.RtCmAnnotationDefn = get_child_object(self.el, "rt", self.tag_dict, class_name="CmAnnotationDefn")
        self.RtCmAnthroItem = get_child_object(self.el, "rt", self.tag_dict, class_name="CmAnthroItem")
        self.RtCmPerson = get_child_object(self.el, "rt", self.tag_dict, class_name="CmPerson")
        self.RtCmPossibility = get_child_object(self.el, "rt", self.tag_dict, class_name="CmPossibility")
        self.RtCmSemanticDomain = get_child_object(self.el, "rt", self.tag_dict, class_name="CmSemanticDomain")
        self.RtLexEntryInflType = get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryInflType")
        self.RtLexEntryType = get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryType")
        self.RtLexRefType = get_child_object(self.el, "rt", self.tag_dict, class_name="LexRefType")
        self.RtMoMorphType = get_child_object(self.el, "rt", self.tag_dict, class_name="MoMorphType")
        self.RtPartOfSpeech = get_child_object(self.el, "rt", self.tag_dict, class_name="PartOfSpeech")
