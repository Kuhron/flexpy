import xml.etree.ElementTree as ET

from flexpy.TagDict import TagDict


class Rt:
    def __init__(self, el, tag_dict):
        assert type(el) is ET.Element, "invalid element: {}".format(el)
        assert el.tag == "rt", "invalid element tag: {}".format(el.tag)
        assert type(tag_dict) is TagDict
        self.rt = el
        self.tag_dict = tag_dict
        self.class_name = el.attrib["class"]
        self.guid = el.attrib.get("guid")
        self.ownerguid = el.attrib.get("ownerguid")
        self.owner_el = tag_dict.get(self.ownerguid)

        # causes max recursion and/or memory leak
        # self.owner = get_python_object_from_element(self.owner_el, tag_dict) if self.owner_el is not None else None

    def get_owner(self):
        # only construct this when asked, otherwise will take up too much memory
        return self.tag_dict.get_python_object_from_element(self.owner_el)

    def __repr__(self):
        return "<rt class={} guid={}>".format(self.class_name, self.guid)