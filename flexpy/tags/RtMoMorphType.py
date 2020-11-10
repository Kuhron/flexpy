from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtMoMorphType(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.ownerguid = self.el.attrib.get(ownerguid)
        self.Abbreviation = get_child_object(self.el, "Abbreviation", self.tag_dict)
        self.BackColor = get_child_object(self.el, "BackColor", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Description = get_child_object(self.el, "Description", self.tag_dict)
        self.Discussion = get_child_object(self.el, "Discussion", self.tag_dict)
        self.ForeColor = get_child_object(self.el, "ForeColor", self.tag_dict)
        self.Hidden = get_child_object(self.el, "Hidden", self.tag_dict)
        self.IsProtected = get_child_object(self.el, "IsProtected", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.Postfix = get_child_object(self.el, "Postfix", self.tag_dict)
        self.Prefix = get_child_object(self.el, "Prefix", self.tag_dict)
        self.SecondaryOrder = get_child_object(self.el, "SecondaryOrder", self.tag_dict)
        self.SortSpec = get_child_object(self.el, "SortSpec", self.tag_dict)
        self.UnderColor = get_child_object(self.el, "UnderColor", self.tag_dict)
        self.UnderStyle = get_child_object(self.el, "UnderStyle", self.tag_dict)
