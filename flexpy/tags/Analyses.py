from flexpy.FlexPyUtil import get_child_object

class Analyses:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.RtPunctuationForm = get_child_object(self.el, "rt", self.tag_dict, class_name="PunctuationForm")
        self.RtWfiAnalysis = get_child_object(self.el, "rt", self.tag_dict, class_name="WfiAnalysis")
        self.RtWfiGloss = get_child_object(self.el, "rt", self.tag_dict, class_name="WfiGloss")
        self.RtWfiWordform = get_child_object(self.el, "rt", self.tag_dict, class_name="WfiWordform")
