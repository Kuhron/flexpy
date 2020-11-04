from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtScripture(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.BookAnnotations = get_child_object(self.rt, "BookAnnotations", self.rt_dict)
        self.Bridge = get_child_object(self.rt, "Bridge", self.rt_dict)
        self.ChapterVerseSepr = get_child_object(self.rt, "ChapterVerseSepr", self.rt_dict)
        self.ConvertCVDigitsOnExport = get_child_object(self.rt, "ConvertCVDigitsOnExport", self.rt_dict)
        self.CrossRefMarkerSymbol = get_child_object(self.rt, "CrossRefMarkerSymbol", self.rt_dict)
        self.CrossRefMarkerType = get_child_object(self.rt, "CrossRefMarkerType", self.rt_dict)
        self.CrossRefsCombinedWithFootnotes = get_child_object(self.rt, "CrossRefsCombinedWithFootnotes", self.rt_dict)
        self.DateCreated = get_child_object(self.rt, "DateCreated", self.rt_dict)
        self.DateModified = get_child_object(self.rt, "DateModified", self.rt_dict)
        self.DisplayCrossRefReference = get_child_object(self.rt, "DisplayCrossRefReference", self.rt_dict)
        self.DisplayFootnoteReference = get_child_object(self.rt, "DisplayFootnoteReference", self.rt_dict)
        self.DisplaySymbolInCrossRef = get_child_object(self.rt, "DisplaySymbolInCrossRef", self.rt_dict)
        self.DisplaySymbolInFootnote = get_child_object(self.rt, "DisplaySymbolInFootnote", self.rt_dict)
        self.FootnoteMarkerSymbol = get_child_object(self.rt, "FootnoteMarkerSymbol", self.rt_dict)
        self.FootnoteMarkerType = get_child_object(self.rt, "FootnoteMarkerType", self.rt_dict)
        self.RefSepr = get_child_object(self.rt, "RefSepr", self.rt_dict)
        self.Resources = get_child_object(self.rt, "Resources", self.rt_dict)
        self.RestartFootnoteBoundary = get_child_object(self.rt, "RestartFootnoteBoundary", self.rt_dict)
        self.RestartFootnoteSequence = get_child_object(self.rt, "RestartFootnoteSequence", self.rt_dict)
        self.ScriptDigitZero = get_child_object(self.rt, "ScriptDigitZero", self.rt_dict)
        self.UseScriptDigits = get_child_object(self.rt, "UseScriptDigits", self.rt_dict)
        self.VerseSepr = get_child_object(self.rt, "VerseSepr", self.rt_dict)
        self.Versification = get_child_object(self.rt, "Versification", self.rt_dict)
