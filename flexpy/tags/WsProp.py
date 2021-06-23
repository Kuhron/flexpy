from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class WsProp:
    """A class for FLEx XML elements with the tag WsProp
    :param el: the `xml.etree.ElementTree.Element object`
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.fontFamily = self.el.attrib.get("fontFamily")
        self.fontsize = self.el.attrib.get("fontsize")
        self.fontsizeUnit = self.el.attrib.get("fontsizeUnit")
        self.fp = self.el.attrib.get("fp")
        self.ws = self.el.attrib.get("ws")

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)
