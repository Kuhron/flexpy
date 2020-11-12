from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtScripture(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def BookAnnotations(self):
        return get_child_object(self.el, "BookAnnotations", self.tag_dict)

    def Bridge(self):
        return get_child_object(self.el, "Bridge", self.tag_dict)

    def ChapterVerseSepr(self):
        return get_child_object(self.el, "ChapterVerseSepr", self.tag_dict)

    def ConvertCVDigitsOnExport(self):
        return get_child_object(self.el, "ConvertCVDigitsOnExport", self.tag_dict)

    def CrossRefMarkerSymbol(self):
        return get_child_object(self.el, "CrossRefMarkerSymbol", self.tag_dict)

    def CrossRefMarkerType(self):
        return get_child_object(self.el, "CrossRefMarkerType", self.tag_dict)

    def CrossRefsCombinedWithFootnotes(self):
        return get_child_object(self.el, "CrossRefsCombinedWithFootnotes", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DisplayCrossRefReference(self):
        return get_child_object(self.el, "DisplayCrossRefReference", self.tag_dict)

    def DisplayFootnoteReference(self):
        return get_child_object(self.el, "DisplayFootnoteReference", self.tag_dict)

    def DisplaySymbolInCrossRef(self):
        return get_child_object(self.el, "DisplaySymbolInCrossRef", self.tag_dict)

    def DisplaySymbolInFootnote(self):
        return get_child_object(self.el, "DisplaySymbolInFootnote", self.tag_dict)

    def FootnoteMarkerSymbol(self):
        return get_child_object(self.el, "FootnoteMarkerSymbol", self.tag_dict)

    def FootnoteMarkerType(self):
        return get_child_object(self.el, "FootnoteMarkerType", self.tag_dict)

    def RefSepr(self):
        return get_child_object(self.el, "RefSepr", self.tag_dict)

    def Resources(self):
        return get_child_object(self.el, "Resources", self.tag_dict)

    def RestartFootnoteBoundary(self):
        return get_child_object(self.el, "RestartFootnoteBoundary", self.tag_dict)

    def RestartFootnoteSequence(self):
        return get_child_object(self.el, "RestartFootnoteSequence", self.tag_dict)

    def ScriptDigitZero(self):
        return get_child_object(self.el, "ScriptDigitZero", self.tag_dict)

    def UseScriptDigits(self):
        return get_child_object(self.el, "UseScriptDigits", self.tag_dict)

    def VerseSepr(self):
        return get_child_object(self.el, "VerseSepr", self.tag_dict)

    def Versification(self):
        return get_child_object(self.el, "Versification", self.tag_dict)
