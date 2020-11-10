from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtText(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.class = self.el.attrib.get(class)
        self.guid = self.el.attrib.get(guid)
        self.Abbreviation = get_child_object(self.el, "Abbreviation", self.tag_dict)
        self.Contents = get_child_object(self.el, "Contents", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.Description = get_child_object(self.el, "Description", self.tag_dict)
        self.IsTranslated = get_child_object(self.el, "IsTranslated", self.tag_dict)
        self.MediaFiles = get_child_object(self.el, "MediaFiles", self.tag_dict)
        self.Name = get_child_object(self.el, "Name", self.tag_dict)
        self.Source = get_child_object(self.el, "Source", self.tag_dict)
