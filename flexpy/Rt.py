import xml.etree.ElementTree as ET
from flexpy.TagDict import TagDict


class Rt:
    def __init__(self, el, tag_dict):
        assert type(el) is ET.Element, "invalid element: {}".format(el)
        assert el.tag == "rt", "invalid element tag: {}".format(el.tag)
        assert type(tag_dict) is TagDict
        self.rt = el
        self.tag_dict = tag_dict
        self.guid = el.attrib.get("guid")
        self.ownerguid = el.attrib.get("ownerguid")
        self.owner = tag_dict.get(self.ownerguid)

