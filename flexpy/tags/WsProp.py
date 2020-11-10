from flexpy.FlexPyUtil import get_child_object

class WsProp:
    def __init__(self, el, tag_dict):
        self.el = el
        self.fontFamily = self.el.attrib.get(fontFamily)
        self.fontsize = self.el.attrib.get(fontsize)
        self.fontsizeUnit = self.el.attrib.get(fontsizeUnit)
        self.ws = self.el.attrib.get(ws)
