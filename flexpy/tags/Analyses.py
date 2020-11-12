from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Analyses:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def RtPunctuationForm(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="PunctuationForm")

    def RtWfiAnalysis(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="WfiAnalysis")

    def RtWfiGloss(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="WfiGloss")

    def RtWfiWordform(self):
        return get_child_object(self.el, "rt", self.tag_dict, class_name="WfiWordform")
