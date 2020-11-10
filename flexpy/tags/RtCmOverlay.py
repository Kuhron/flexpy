from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmOverlay(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.PossItems = get_child_object(self.el, "PossItems", self.tag_dict)
        self.PossList = get_child_object(self.el, "PossList", self.tag_dict)
