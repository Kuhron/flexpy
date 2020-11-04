class Rt:
    def __init__(self, el, rt_dict):
        self.rt = el
        self.rt_dict = rt_dict
        self.guid = el.attrib.get("guid")
        self.ownerguid = el.attrib.get("ownerguid")
        self.owner = rt_dict.get(self.ownerguid)

