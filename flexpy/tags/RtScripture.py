from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScripture(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.BookAnnotations = get_child_object(self.el, "BookAnnotations", self.tag_dict)
        self.Bridge = get_child_object(self.el, "Bridge", self.tag_dict)
        self.ChapterVerseSepr = get_child_object(self.el, "ChapterVerseSepr", self.tag_dict)
        self.ConvertCVDigitsOnExport = get_child_object(self.el, "ConvertCVDigitsOnExport", self.tag_dict)
        self.CrossRefMarkerSymbol = get_child_object(self.el, "CrossRefMarkerSymbol", self.tag_dict)
        self.CrossRefMarkerType = get_child_object(self.el, "CrossRefMarkerType", self.tag_dict)
        self.CrossRefsCombinedWithFootnotes = get_child_object(self.el, "CrossRefsCombinedWithFootnotes", self.tag_dict)
        self.DateCreated = get_child_object(self.el, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.el, "DateModified", self.tag_dict)
        self.DisplayCrossRefReference = get_child_object(self.el, "DisplayCrossRefReference", self.tag_dict)
        self.DisplayFootnoteReference = get_child_object(self.el, "DisplayFootnoteReference", self.tag_dict)
        self.DisplaySymbolInCrossRef = get_child_object(self.el, "DisplaySymbolInCrossRef", self.tag_dict)
        self.DisplaySymbolInFootnote = get_child_object(self.el, "DisplaySymbolInFootnote", self.tag_dict)
        self.FootnoteMarkerSymbol = get_child_object(self.el, "FootnoteMarkerSymbol", self.tag_dict)
        self.FootnoteMarkerType = get_child_object(self.el, "FootnoteMarkerType", self.tag_dict)
        self.RefSepr = get_child_object(self.el, "RefSepr", self.tag_dict)
        self.Resources = get_child_object(self.el, "Resources", self.tag_dict)
        self.RestartFootnoteBoundary = get_child_object(self.el, "RestartFootnoteBoundary", self.tag_dict)
        self.RestartFootnoteSequence = get_child_object(self.el, "RestartFootnoteSequence", self.tag_dict)
        self.ScriptDigitZero = get_child_object(self.el, "ScriptDigitZero", self.tag_dict)
        self.UseScriptDigits = get_child_object(self.el, "UseScriptDigits", self.tag_dict)
        self.VerseSepr = get_child_object(self.el, "VerseSepr", self.tag_dict)
        self.Versification = get_child_object(self.el, "Versification", self.tag_dict)
