from flexpy.FlexPyUtil import get_child_object

class SubPossibilities:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtCmAnnotationDefn = get_child_object(self.el, "rt", self.tag_dict, class_name="CmAnnotationDefn")
        self.RtCmAnthroItem = get_child_object(self.el, "rt", self.tag_dict, class_name="CmAnthroItem")
        self.RtCmPossibility = get_child_object(self.el, "rt", self.tag_dict, class_name="CmPossibility")
        self.RtCmSemanticDomain = get_child_object(self.el, "rt", self.tag_dict, class_name="CmSemanticDomain")
        self.RtLexEntryInflType = get_child_object(self.el, "rt", self.tag_dict, class_name="LexEntryInflType")
        self.RtPartOfSpeech = get_child_object(self.el, "rt", self.tag_dict, class_name="PartOfSpeech")
