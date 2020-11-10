from flexpy.FlexPyUtil import get_child_object

class Next:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtStStyle = get_child_object(self.el, "rt", self.tag_dict, class_name="StStyle")
