from flexpy.FlexPyUtil import get_child_object

class Run:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.link = self.el.attrib.get("link")
        self.namedStyle = self.el.attrib.get("namedStyle")
        self.spellcheck = self.el.attrib.get("spellcheck")
        self.ws = self.el.attrib.get("ws")
