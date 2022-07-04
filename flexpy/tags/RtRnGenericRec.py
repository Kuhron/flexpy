from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtRnGenericRec(Rt):
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

    def AnthroCodes(self):
        """Gets the child objects which have short tag of `AnthroCodes`, long tag of `AnthroCodes`"""
        return get_child_object(self.el, "AnthroCodes", self.tag_dict)

    def Conclusions(self):
        """Gets the child objects which have short tag of `Conclusions`, long tag of `Conclusions`"""
        return get_child_object(self.el, "Conclusions", self.tag_dict)

    def DateCreated(self):
        """Gets the child objects which have short tag of `DateCreated`, long tag of `DateCreated`"""
        return get_child_object(self.el, "DateCreated", self.tag_dict)

    def DateModified(self):
        """Gets the child objects which have short tag of `DateModified`, long tag of `DateModified`"""
        return get_child_object(self.el, "DateModified", self.tag_dict)

    def DateOfEvent(self):
        """Gets the child objects which have short tag of `DateOfEvent`, long tag of `DateOfEvent`"""
        return get_child_object(self.el, "DateOfEvent", self.tag_dict)

    def Description(self):
        """Gets the child objects which have short tag of `Description`, long tag of `Description`"""
        return get_child_object(self.el, "Description", self.tag_dict)

    def Discussion(self):
        """Gets the child objects which have short tag of `Discussion`, long tag of `Discussion`"""
        return get_child_object(self.el, "Discussion", self.tag_dict)

    def ExternalMaterials(self):
        """Gets the child objects which have short tag of `ExternalMaterials`, long tag of `ExternalMaterials`"""
        return get_child_object(self.el, "ExternalMaterials", self.tag_dict)

    def FurtherQuestions(self):
        """Gets the child objects which have short tag of `FurtherQuestions`, long tag of `FurtherQuestions`"""
        return get_child_object(self.el, "FurtherQuestions", self.tag_dict)

    def Hypothesis(self):
        """Gets the child objects which have short tag of `Hypothesis`, long tag of `Hypothesis`"""
        return get_child_object(self.el, "Hypothesis", self.tag_dict)

    def Locations(self):
        """Gets the child objects which have short tag of `Locations`, long tag of `Locations`"""
        return get_child_object(self.el, "Locations", self.tag_dict)

    def Participants(self):
        """Gets the child objects which have short tag of `Participants`, long tag of `Participants`"""
        return get_child_object(self.el, "Participants", self.tag_dict)

    def PersonalNotes(self):
        """Gets the child objects which have short tag of `PersonalNotes`, long tag of `PersonalNotes`"""
        return get_child_object(self.el, "PersonalNotes", self.tag_dict)

    def ResearchPlan(self):
        """Gets the child objects which have short tag of `ResearchPlan`, long tag of `ResearchPlan`"""
        return get_child_object(self.el, "ResearchPlan", self.tag_dict)

    def Researchers(self):
        """Gets the child objects which have short tag of `Researchers`, long tag of `Researchers`"""
        return get_child_object(self.el, "Researchers", self.tag_dict)

    def Sources(self):
        """Gets the child objects which have short tag of `Sources`, long tag of `Sources`"""
        return get_child_object(self.el, "Sources", self.tag_dict)

    def Text(self):
        """Gets the child objects which have short tag of `Text`, long tag of `Text`"""
        return get_child_object(self.el, "Text", self.tag_dict)

    def Title(self):
        """Gets the child objects which have short tag of `Title`, long tag of `Title`"""
        return get_child_object(self.el, "Title", self.tag_dict)

    def Type(self):
        """Gets the child objects which have short tag of `Type`, long tag of `Type`"""
        return get_child_object(self.el, "Type", self.tag_dict)

    def VersionHistory(self):
        """Gets the child objects which have short tag of `VersionHistory`, long tag of `VersionHistory`"""
        return get_child_object(self.el, "VersionHistory", self.tag_dict)
