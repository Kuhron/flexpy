from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtLangProject(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def AffixCategories(self):
        return get_child_object(self.el, "AffixCategories", self.tag_dict)

    def AnalysisWss(self):
        return get_child_object(self.el, "AnalysisWss", self.tag_dict)

    def AnalyzingAgents(self):
        return get_child_object(self.el, "AnalyzingAgents", self.tag_dict)

    def AnnotationDefs(self):
        return get_child_object(self.el, "AnnotationDefs", self.tag_dict)

    def Annotations(self):
        return get_child_object(self.el, "Annotations", self.tag_dict)

    def AnthroList(self):
        return get_child_object(self.el, "AnthroList", self.tag_dict)

    def ConfidenceLevels(self):
        return get_child_object(self.el, "ConfidenceLevels", self.tag_dict)

    def CurAnalysisWss(self):
        return get_child_object(self.el, "CurAnalysisWss", self.tag_dict)

    def CurPronunWss(self):
        return get_child_object(self.el, "CurPronunWss", self.tag_dict)

    def CurVernWss(self):
        return get_child_object(self.el, "CurVernWss", self.tag_dict)

    def DateCreated(self):
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DiscourseData(self):
        return get_child_object(self.el, "DiscourseData", self.tag_dict)

    def Education(self):
        return get_child_object(self.el, "Education", self.tag_dict)

    def FilePathsInTsStrings(self):
        return get_child_object(self.el, "FilePathsInTsStrings", self.tag_dict)

    def Filters(self):
        return get_child_object(self.el, "Filters", self.tag_dict)

    def GenreList(self):
        return get_child_object(self.el, "GenreList", self.tag_dict)

    def HomographWs(self):
        return get_child_object(self.el, "HomographWs", self.tag_dict)

    def LexDb(self):
        return get_child_object(self.el, "LexDb", self.tag_dict)

    def Locations(self):
        return get_child_object(self.el, "Locations", self.tag_dict)

    def MorphologicalData(self):
        return get_child_object(self.el, "MorphologicalData", self.tag_dict)

    def MsFeatureSystem(self):
        return get_child_object(self.el, "MsFeatureSystem", self.tag_dict)

    def Overlays(self):
        return get_child_object(self.el, "Overlays", self.tag_dict)

    def PartsOfSpeech(self):
        return get_child_object(self.el, "PartsOfSpeech", self.tag_dict)

    def People(self):
        return get_child_object(self.el, "People", self.tag_dict)

    def PhFeatureSystem(self):
        return get_child_object(self.el, "PhFeatureSystem", self.tag_dict)

    def PhonologicalData(self):
        return get_child_object(self.el, "PhonologicalData", self.tag_dict)

    def Positions(self):
        return get_child_object(self.el, "Positions", self.tag_dict)

    def ResearchNotebook(self):
        return get_child_object(self.el, "ResearchNotebook", self.tag_dict)

    def Restrictions(self):
        return get_child_object(self.el, "Restrictions", self.tag_dict)

    def Roles(self):
        return get_child_object(self.el, "Roles", self.tag_dict)

    def SemanticDomainList(self):
        return get_child_object(self.el, "SemanticDomainList", self.tag_dict)

    def Status(self):
        return get_child_object(self.el, "Status", self.tag_dict)

    def Styles(self):
        return get_child_object(self.el, "Styles", self.tag_dict)

    def TextMarkupTags(self):
        return get_child_object(self.el, "TextMarkupTags", self.tag_dict)

    def TimeOfDay(self):
        return get_child_object(self.el, "TimeOfDay", self.tag_dict)

    def TranslatedScripture(self):
        return get_child_object(self.el, "TranslatedScripture", self.tag_dict)

    def TranslationTags(self):
        return get_child_object(self.el, "TranslationTags", self.tag_dict)

    def VernWss(self):
        return get_child_object(self.el, "VernWss", self.tag_dict)
