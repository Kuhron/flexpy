class Rt:
    def __init__(self, el, tag_dict):
        self.rt = el
        self.tag_dict = tag_dict
        self.guid = el.attrib.get("guid")
        self.ownerguid = el.attrib.get("ownerguid")
        self.owner = tag_dict.get(self.ownerguid)

