from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtCmAnnotationDefn(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.Abbreviation = get_child_object(self.el, "Abbreviation", self.tag_dict)
        self.AllowsComment = get_child_object(self.el, "AllowsComment", self.tag_dict)
        self.AllowsFeatureStructure = get_child_object(self.el, "AllowsFeatureStructure", self.tag_dict)
        self.AllowsInstanceOf = get_child_object(self.el, "AllowsInstanceOf", self.tag_dict)
        self.BackColor = get_child_object(self.el, "BackColor", self.tag_dict)
        self.CanCreateOrphan = get_child_object(self.el, "CanCreateOrphan", self.tag_dict)
        self.CopyCutPastable = get_child_object(self.el, "CopyCutPastable", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Description = get_child_object(self.el, "Description", self.tag_dict)
        self.Discussion = get_child_object(self.el, "Discussion", self.tag_dict)
        self.ForeColor = get_child_object(self.el, "ForeColor", self.tag_dict)
        self.Hidden = get_child_object(self.el, "Hidden", self.tag_dict)
        self.InstanceOfSignature = get_child_object(self.el, "InstanceOfSignature", self.tag_dict)
        self.IsProtected = get_child_object(self.el, "IsProtected", self.tag_dict)
        self.MaxDupOccur = get_child_object(self.el, "MaxDupOccur", self.tag_dict)
        self.Multi = get_child_object(self.el, "Multi", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.PromptUser = get_child_object(self.el, "PromptUser", self.tag_dict)
        self.Severity = get_child_object(self.el, "Severity", self.tag_dict)
        self.SortSpec = get_child_object(self.el, "SortSpec", self.tag_dict)
        self.SubPossibilities = get_child_object(self.el, "SubPossibilities", self.tag_dict)
        self.UnderColor = get_child_object(self.el, "UnderColor", self.tag_dict)
        self.UnderStyle = get_child_object(self.el, "UnderStyle", self.tag_dict)
        self.UserCanCreate = get_child_object(self.el, "UserCanCreate", self.tag_dict)
        self.ZeroWidth = get_child_object(self.el, "ZeroWidth", self.tag_dict)
