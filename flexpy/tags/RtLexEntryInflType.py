from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLexEntryInflType(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Abbreviation(self):
        return get_child_object(self.el, "Abbreviation", self.tag_dict)

    def BackColor(self):
        return get_child_object(self.el, "BackColor", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def Description(self):
        return get_child_object(self.el, "Description", self.tag_dict)

    def Discussion(self):
        return get_child_object(self.el, "Discussion", self.tag_dict)

    def ForeColor(self):
        return get_child_object(self.el, "ForeColor", self.tag_dict)

    def GlossAppend(self):
        return get_child_object(self.el, "GlossAppend", self.tag_dict)

    def Hidden(self):
        return get_child_object(self.el, "Hidden", self.tag_dict)

    def IsProtected(self):
        return get_child_object(self.el, "IsProtected", self.tag_dict)

    def Name(self):
        return get_child_object(self.el, "Name", self.tag_dict)

    def ReverseAbbr(self):
        return get_child_object(self.el, "ReverseAbbr", self.tag_dict)

    def ReverseName(self):
        return get_child_object(self.el, "ReverseName", self.tag_dict)

    def SortSpec(self):
        return get_child_object(self.el, "SortSpec", self.tag_dict)

    def SubPossibilities(self):
        return get_child_object(self.el, "SubPossibilities", self.tag_dict)

    def UnderColor(self):
        return get_child_object(self.el, "UnderColor", self.tag_dict)

    def UnderStyle(self):
        return get_child_object(self.el, "UnderStyle", self.tag_dict)
