from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtScripture(Rt):
    """A class for FLEx XML elements with the tag rt
    :param el: the `xml.etree.ElementTree.Element object`
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def BookAnnotations(self):
        """Gets the child objects which have short tag of `BookAnnotations`, long tag of `BookAnnotations`"""
        return get_child_object(self.el, "BookAnnotations", self.tag_dict)

    def Bridge(self):
        """Gets the child objects which have short tag of `Bridge`, long tag of `Bridge`"""
        return get_child_object(self.el, "Bridge", self.tag_dict)

    def ChapterVerseSepr(self):
        """Gets the child objects which have short tag of `ChapterVerseSepr`, long tag of `ChapterVerseSepr`"""
        return get_child_object(self.el, "ChapterVerseSepr", self.tag_dict)

    def ConvertCVDigitsOnExport(self):
        """Gets the child objects which have short tag of `ConvertCVDigitsOnExport`, long tag of `ConvertCVDigitsOnExport`"""
        return get_child_object(self.el, "ConvertCVDigitsOnExport", self.tag_dict)

    def CrossRefMarkerSymbol(self):
        """Gets the child objects which have short tag of `CrossRefMarkerSymbol`, long tag of `CrossRefMarkerSymbol`"""
        return get_child_object(self.el, "CrossRefMarkerSymbol", self.tag_dict)

    def CrossRefMarkerType(self):
        """Gets the child objects which have short tag of `CrossRefMarkerType`, long tag of `CrossRefMarkerType`"""
        return get_child_object(self.el, "CrossRefMarkerType", self.tag_dict)

    def CrossRefsCombinedWithFootnotes(self):
        """Gets the child objects which have short tag of `CrossRefsCombinedWithFootnotes`, long tag of `CrossRefsCombinedWithFootnotes`"""
        return get_child_object(self.el, "CrossRefsCombinedWithFootnotes", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DisplayCrossRefReference(self):
        """Gets the child objects which have short tag of `DisplayCrossRefReference`, long tag of `DisplayCrossRefReference`"""
        return get_child_object(self.el, "DisplayCrossRefReference", self.tag_dict)

    def DisplayFootnoteReference(self):
        """Gets the child objects which have short tag of `DisplayFootnoteReference`, long tag of `DisplayFootnoteReference`"""
        return get_child_object(self.el, "DisplayFootnoteReference", self.tag_dict)

    def DisplaySymbolInCrossRef(self):
        """Gets the child objects which have short tag of `DisplaySymbolInCrossRef`, long tag of `DisplaySymbolInCrossRef`"""
        return get_child_object(self.el, "DisplaySymbolInCrossRef", self.tag_dict)

    def DisplaySymbolInFootnote(self):
        """Gets the child objects which have short tag of `DisplaySymbolInFootnote`, long tag of `DisplaySymbolInFootnote`"""
        return get_child_object(self.el, "DisplaySymbolInFootnote", self.tag_dict)

    def FootnoteMarkerSymbol(self):
        """Gets the child objects which have short tag of `FootnoteMarkerSymbol`, long tag of `FootnoteMarkerSymbol`"""
        return get_child_object(self.el, "FootnoteMarkerSymbol", self.tag_dict)

    def FootnoteMarkerType(self):
        """Gets the child objects which have short tag of `FootnoteMarkerType`, long tag of `FootnoteMarkerType`"""
        return get_child_object(self.el, "FootnoteMarkerType", self.tag_dict)

    def RefSepr(self):
        """Gets the child objects which have short tag of `RefSepr`, long tag of `RefSepr`"""
        return get_child_object(self.el, "RefSepr", self.tag_dict)

    def Resources(self):
        """Gets the child objects which have short tag of `Resources`, long tag of `Resources`"""
        return get_child_object(self.el, "Resources", self.tag_dict)

    def RestartFootnoteBoundary(self):
        """Gets the child objects which have short tag of `RestartFootnoteBoundary`, long tag of `RestartFootnoteBoundary`"""
        return get_child_object(self.el, "RestartFootnoteBoundary", self.tag_dict)

    def RestartFootnoteSequence(self):
        """Gets the child objects which have short tag of `RestartFootnoteSequence`, long tag of `RestartFootnoteSequence`"""
        return get_child_object(self.el, "RestartFootnoteSequence", self.tag_dict)

    def ScriptDigitZero(self):
        """Gets the child objects which have short tag of `ScriptDigitZero`, long tag of `ScriptDigitZero`"""
        return get_child_object(self.el, "ScriptDigitZero", self.tag_dict)

    def UseScriptDigits(self):
        """Gets the child objects which have short tag of `UseScriptDigits`, long tag of `UseScriptDigits`"""
        return get_child_object(self.el, "UseScriptDigits", self.tag_dict)

    def VerseSepr(self):
        """Gets the child objects which have short tag of `VerseSepr`, long tag of `VerseSepr`"""
        return get_child_object(self.el, "VerseSepr", self.tag_dict)

    def Versification(self):
        """Gets the child objects which have short tag of `Versification`, long tag of `Versification`"""
        return get_child_object(self.el, "Versification", self.tag_dict)
