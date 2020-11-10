from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtStTxtPara(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.Contents = get_child_object(self.el, "Contents", self.tag_dict)
        self.ParseIsCurrent = get_child_object(self.el, "ParseIsCurrent", self.tag_dict)
        self.Segments = get_child_object(self.el, "Segments", self.tag_dict)
        self.StyleRules = get_child_object(self.el, "StyleRules", self.tag_dict)
