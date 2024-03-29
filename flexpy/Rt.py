import xml.etree.ElementTree as ET

from flexpy.TagDict import TagDict
from flexpy.FlexPyUtil import elstr, selstr


class Rt:
    """A FlexPy-specific class mean to hold information about XML elements with the tag `rt`,
    which have various class names assigned by FLEx.
    """
    def __init__(self, el, tag_dict, parent_el=None):
        assert type(el) is ET.Element, f"invalid element: {el}"
        assert el.tag == "rt", f"invalid element tag: {el.tag}"
        if parent_el is not None:
            assert type(parent_el) is ET.Element, f"invalid parent element: {parent_el}"
        assert type(tag_dict) is TagDict
        self.rt = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.class_name = el.attrib["class"]
        self.guid = el.attrib.get("guid")
        self.ownerguid = el.attrib.get("ownerguid")
        self.owner_el = tag_dict.get_single_element_by_guid(self.ownerguid)
        assert self.owner_el is None or type(self.owner_el) is ET.Element, self.owner_el


        # causes max recursion and/or memory leak
        # self.owner = get_python_object_from_element(self.owner_el, tag_dict) if self.owner_el is not None else None

    def get_owner(self):
        # only construct this when asked, otherwise will take up too much memory
        return self.tag_dict.get_python_object_from_element(self.owner_el)

    def __repr__(self):
        return selstr(self.el)