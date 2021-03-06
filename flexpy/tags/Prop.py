from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Prop:
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.align = self.el.attrib.get("align")
        self.bold = self.el.attrib.get("bold")
        self.bulNumScheme = self.el.attrib.get("bulNumScheme")
        self.bulNumStartAt = self.el.attrib.get("bulNumStartAt")
        self.firstIndent = self.el.attrib.get("firstIndent")
        self.fontsize = self.el.attrib.get("fontsize")
        self.fontsizeUnit = self.el.attrib.get("fontsizeUnit")
        self.forecolor = self.el.attrib.get("forecolor")
        self.italic = self.el.attrib.get("italic")
        self.keepTogether = self.el.attrib.get("keepTogether")
        self.keepWithNext = self.el.attrib.get("keepWithNext")
        self.leadingIndent = self.el.attrib.get("leadingIndent")
        self.lineHeight = self.el.attrib.get("lineHeight")
        self.lineHeightType = self.el.attrib.get("lineHeightType")
        self.lineHeightUnit = self.el.attrib.get("lineHeightUnit")
        self.namedStyle = self.el.attrib.get("namedStyle")
        self.spaceAfter = self.el.attrib.get("spaceAfter")
        self.spaceBefore = self.el.attrib.get("spaceBefore")
        self.spellcheck = self.el.attrib.get("spellcheck")
        self.superscript = self.el.attrib.get("superscript")
        self.trailingIndent = self.el.attrib.get("trailingIndent")
        self.undercolor = self.el.attrib.get("undercolor")
        self.underline = self.el.attrib.get("underline")

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def WsStyles9999(self):
        return get_child_object(self.el, "WsStyles9999", self.tag_dict)
