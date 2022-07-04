from flexpy.NonRtTag import NonRtTag
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class Run(NonRtTag):
    """A class for FLEx XML elements with the tag Run

    :param el: the `xml.etree.ElementTree.Element` object
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, parent_el=None, tag_dict=None):
        super().__init__(el, parent_el=parent_el, tag_dict=tag_dict)
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.bold = self.el.attrib.get("bold")
        self.bulNumStartAt = self.el.attrib.get("bulNumStartAt")
        self.fp = self.el.attrib.get("fp")
        self.link = self.el.attrib.get("link")
        self.namedStyle = self.el.attrib.get("namedStyle")
        self.space = self.el.attrib.get("space")
        self.spellcheck = self.el.attrib.get("spellcheck")
        self.undercolor = self.el.attrib.get("undercolor")
        self.underline = self.el.attrib.get("underline")
        self.ws = self.el.attrib.get("ws")

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)
