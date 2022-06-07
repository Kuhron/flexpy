from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLangProject(Rt):
    """A class for FLEx XML elements with the tag rt

    :param el: the `xml.etree.ElementTree.Element` object
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, parent_el=None, tag_dict=None):
        super().__init__(el, parent_el=parent_el, tag_dict=tag_dict)
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def AffixCategories(self):
        """Gets the child objects which have short tag of `AffixCategories`, long tag of `AffixCategories`"""
        return get_child_object(self.el, "AffixCategories", self.tag_dict)

    def AnalysisWss(self):
        """Gets the child objects which have short tag of `AnalysisWss`, long tag of `AnalysisWss`"""
        return get_child_object(self.el, "AnalysisWss", self.tag_dict)

    def AnalyzingAgents(self):
        """Gets the child objects which have short tag of `AnalyzingAgents`, long tag of `AnalyzingAgents`"""
        return get_child_object(self.el, "AnalyzingAgents", self.tag_dict)

    def AnnotationDefs(self):
        """Gets the child objects which have short tag of `AnnotationDefs`, long tag of `AnnotationDefs`"""
        return get_child_object(self.el, "AnnotationDefs", self.tag_dict)

    def AnthroList(self):
        """Gets the child objects which have short tag of `AnthroList`, long tag of `AnthroList`"""
        return get_child_object(self.el, "AnthroList", self.tag_dict)

    def ConfidenceLevels(self):
        """Gets the child objects which have short tag of `ConfidenceLevels`, long tag of `ConfidenceLevels`"""
        return get_child_object(self.el, "ConfidenceLevels", self.tag_dict)

    def CurAnalysisWss(self):
        """Gets the child objects which have short tag of `CurAnalysisWss`, long tag of `CurAnalysisWss`"""
        return get_child_object(self.el, "CurAnalysisWss", self.tag_dict)

    def CurPronunWss(self):
        """Gets the child objects which have short tag of `CurPronunWss`, long tag of `CurPronunWss`"""
        return get_child_object(self.el, "CurPronunWss", self.tag_dict)

    def CurVernWss(self):
        """Gets the child objects which have short tag of `CurVernWss`, long tag of `CurVernWss`"""
        return get_child_object(self.el, "CurVernWss", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DiscourseData(self):
        """Gets the child objects which have short tag of `DiscourseData`, long tag of `DiscourseData`"""
        return get_child_object(self.el, "DiscourseData", self.tag_dict)

    def Education(self):
        """Gets the child objects which have short tag of `Education`, long tag of `Education`"""
        return get_child_object(self.el, "Education", self.tag_dict)

    def FilePathsInTsStrings(self):
        """Gets the child objects which have short tag of `FilePathsInTsStrings`, long tag of `FilePathsInTsStrings`"""
        return get_child_object(self.el, "FilePathsInTsStrings", self.tag_dict)

    def Filters(self):
        """Gets the child objects which have short tag of `Filters`, long tag of `Filters`"""
        return get_child_object(self.el, "Filters", self.tag_dict)

    def GenreList(self):
        """Gets the child objects which have short tag of `GenreList`, long tag of `GenreList`"""
        return get_child_object(self.el, "GenreList", self.tag_dict)

    def HomographWs(self):
        """Gets the child objects which have short tag of `HomographWs`, long tag of `HomographWs`"""
        return get_child_object(self.el, "HomographWs", self.tag_dict)

    def LexDb(self):
        """Gets the child objects which have short tag of `LexDb`, long tag of `LexDb`"""
        return get_child_object(self.el, "LexDb", self.tag_dict)

    def LinkedFilesRootDir(self):
        """Gets the child objects which have short tag of `LinkedFilesRootDir`, long tag of `LinkedFilesRootDir`"""
        return get_child_object(self.el, "LinkedFilesRootDir", self.tag_dict)

    def Locations(self):
        """Gets the child objects which have short tag of `Locations`, long tag of `Locations`"""
        return get_child_object(self.el, "Locations", self.tag_dict)

    def MorphologicalData(self):
        """Gets the child objects which have short tag of `MorphologicalData`, long tag of `MorphologicalData`"""
        return get_child_object(self.el, "MorphologicalData", self.tag_dict)

    def MsFeatureSystem(self):
        """Gets the child objects which have short tag of `MsFeatureSystem`, long tag of `MsFeatureSystem`"""
        return get_child_object(self.el, "MsFeatureSystem", self.tag_dict)

    def Overlays(self):
        """Gets the child objects which have short tag of `Overlays`, long tag of `Overlays`"""
        return get_child_object(self.el, "Overlays", self.tag_dict)

    def PartsOfSpeech(self):
        """Gets the child objects which have short tag of `PartsOfSpeech`, long tag of `PartsOfSpeech`"""
        return get_child_object(self.el, "PartsOfSpeech", self.tag_dict)

    def People(self):
        """Gets the child objects which have short tag of `People`, long tag of `People`"""
        return get_child_object(self.el, "People", self.tag_dict)

    def PhFeatureSystem(self):
        """Gets the child objects which have short tag of `PhFeatureSystem`, long tag of `PhFeatureSystem`"""
        return get_child_object(self.el, "PhFeatureSystem", self.tag_dict)

    def PhonologicalData(self):
        """Gets the child objects which have short tag of `PhonologicalData`, long tag of `PhonologicalData`"""
        return get_child_object(self.el, "PhonologicalData", self.tag_dict)

    def Positions(self):
        """Gets the child objects which have short tag of `Positions`, long tag of `Positions`"""
        return get_child_object(self.el, "Positions", self.tag_dict)

    def ResearchNotebook(self):
        """Gets the child objects which have short tag of `ResearchNotebook`, long tag of `ResearchNotebook`"""
        return get_child_object(self.el, "ResearchNotebook", self.tag_dict)

    def Restrictions(self):
        """Gets the child objects which have short tag of `Restrictions`, long tag of `Restrictions`"""
        return get_child_object(self.el, "Restrictions", self.tag_dict)

    def Roles(self):
        """Gets the child objects which have short tag of `Roles`, long tag of `Roles`"""
        return get_child_object(self.el, "Roles", self.tag_dict)

    def SemanticDomainList(self):
        """Gets the child objects which have short tag of `SemanticDomainList`, long tag of `SemanticDomainList`"""
        return get_child_object(self.el, "SemanticDomainList", self.tag_dict)

    def Status(self):
        """Gets the child objects which have short tag of `Status`, long tag of `Status`"""
        return get_child_object(self.el, "Status", self.tag_dict)

    def Styles(self):
        """Gets the child objects which have short tag of `Styles`, long tag of `Styles`"""
        return get_child_object(self.el, "Styles", self.tag_dict)

    def TextMarkupTags(self):
        """Gets the child objects which have short tag of `TextMarkupTags`, long tag of `TextMarkupTags`"""
        return get_child_object(self.el, "TextMarkupTags", self.tag_dict)

    def TimeOfDay(self):
        """Gets the child objects which have short tag of `TimeOfDay`, long tag of `TimeOfDay`"""
        return get_child_object(self.el, "TimeOfDay", self.tag_dict)

    def TranslatedScripture(self):
        """Gets the child objects which have short tag of `TranslatedScripture`, long tag of `TranslatedScripture`"""
        return get_child_object(self.el, "TranslatedScripture", self.tag_dict)

    def TranslationTags(self):
        """Gets the child objects which have short tag of `TranslationTags`, long tag of `TranslationTags`"""
        return get_child_object(self.el, "TranslationTags", self.tag_dict)

    def VernWss(self):
        """Gets the child objects which have short tag of `VernWss`, long tag of `VernWss`"""
        return get_child_object(self.el, "VernWss", self.tag_dict)
