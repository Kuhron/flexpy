from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtCmSemanticDomain(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.child_objects = get_ordered_child_objects(el, tag_dict)
        self.Abbreviation = get_child_object(self.el, "Abbreviation", self.tag_dict)
        self.BackColor = get_child_object(self.el, "BackColor", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Description = get_child_object(self.el, "Description", self.tag_dict)
        self.Discussion = get_child_object(self.el, "Discussion", self.tag_dict)
        self.ForeColor = get_child_object(self.el, "ForeColor", self.tag_dict)
        self.Hidden = get_child_object(self.el, "Hidden", self.tag_dict)
        self.IsProtected = get_child_object(self.el, "IsProtected", self.tag_dict)
        self.LouwNidaCodes = get_child_object(self.el, "LouwNidaCodes", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.OcmCodes = get_child_object(self.el, "OcmCodes", self.tag_dict)
        self.Questions = get_child_object(self.el, "Questions", self.tag_dict)
        self.RelatedDomains = get_child_object(self.el, "RelatedDomains", self.tag_dict)
        self.SortSpec = get_child_object(self.el, "SortSpec", self.tag_dict)
        self.SubPossibilities = get_child_object(self.el, "SubPossibilities", self.tag_dict)
        self.UnderColor = get_child_object(self.el, "UnderColor", self.tag_dict)
        self.UnderStyle = get_child_object(self.el, "UnderStyle", self.tag_dict)
