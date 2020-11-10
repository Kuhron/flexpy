from flexpy.FlexPyUtil import get_child_object

class AUni:
    def __init__(self, el, tag_dict):
        self.el = el
        self.ws = self.el.attrib.get(ws)
