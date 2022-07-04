import xml.etree.ElementTree as ET

from flexpy.TagDict import TagDict
from flexpy.FlexPyUtil import elstr, selstr


class NonRtTag:
    """A FlexPy-specific class mean to hold information about XML elements with tags other than `rt`,
    which have various class names assigned by FLEx.
    """
    def __init__(self, el, parent_el, tag_dict):
        assert type(el) is ET.Element, f"invalid element: {el}"
        assert type(parent_el) is ET.Element, f"invalid parent element: {parent_el} of element {elstr(el)}"
        assert type(tag_dict) is TagDict
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict

    def __repr__(self):
        return f"<tag={self.el.tag} parent={selstr(self.parent_el)}>"

