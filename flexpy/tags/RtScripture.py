from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScripture(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.BookAnnotations = get_child_object(self.rt, "BookAnnotations", self.tag_dict)
        self.Bridge = get_child_object(self.rt, "Bridge", self.tag_dict)
        self.ChapterVerseSepr = get_child_object(self.rt, "ChapterVerseSepr", self.tag_dict)
        self.ConvertCVDigitsOnExport = get_child_object(self.rt, "ConvertCVDigitsOnExport", self.tag_dict)
        self.CrossRefMarkerSymbol = get_child_object(self.rt, "CrossRefMarkerSymbol", self.tag_dict)
        self.CrossRefMarkerType = get_child_object(self.rt, "CrossRefMarkerType", self.tag_dict)
        self.CrossRefsCombinedWithFootnotes = get_child_object(self.rt, "CrossRefsCombinedWithFootnotes", self.tag_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.tag_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.tag_dict)
        self.DisplayCrossRefReference = get_child_object(self.rt, "DisplayCrossRefReference", self.tag_dict)
        self.DisplayFootnoteReference = get_child_object(self.rt, "DisplayFootnoteReference", self.tag_dict)
        self.DisplaySymbolInCrossRef = get_child_object(self.rt, "DisplaySymbolInCrossRef", self.tag_dict)
        self.DisplaySymbolInFootnote = get_child_object(self.rt, "DisplaySymbolInFootnote", self.tag_dict)
        self.FootnoteMarkerSymbol = get_child_object(self.rt, "FootnoteMarkerSymbol", self.tag_dict)
        self.FootnoteMarkerType = get_child_object(self.rt, "FootnoteMarkerType", self.tag_dict)
        self.RefSepr = get_child_object(self.rt, "RefSepr", self.tag_dict)
        self.Resources = get_child_object(self.rt, "Resources", self.tag_dict)
        self.RestartFootnoteBoundary = get_child_object(self.rt, "RestartFootnoteBoundary", self.tag_dict)
        self.RestartFootnoteSequence = get_child_object(self.rt, "RestartFootnoteSequence", self.tag_dict)
        self.ScriptDigitZero = get_child_object(self.rt, "ScriptDigitZero", self.tag_dict)
        self.UseScriptDigits = get_child_object(self.rt, "UseScriptDigits", self.tag_dict)
        self.VerseSepr = get_child_object(self.rt, "VerseSepr", self.tag_dict)
        self.Versification = get_child_object(self.rt, "Versification", self.tag_dict)
