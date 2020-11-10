from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtMoMorphData(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.ParserParameters = get_child_object(self.el, "ParserParameters", self.tag_dict)
        self.ProdRestrict = get_child_object(self.el, "ProdRestrict", self.tag_dict)
