from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmMediaContainer(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.MediaURIs = get_child_object(self.el, "MediaURIs", self.tag_dict)
