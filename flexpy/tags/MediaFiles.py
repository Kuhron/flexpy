from flexpy.FlexPyUtil import get_child_object

class MediaFiles:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtCmMediaContainer = get_child_object(self.el, "rt", self.tag_dict, class_name="CmMediaContainer")
