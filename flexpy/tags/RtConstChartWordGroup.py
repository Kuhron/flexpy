from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtConstChartWordGroup(Rt):
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

    def BeginAnalysisIndex(self):
        """Gets the child objects which have short tag of `BeginAnalysisIndex`, long tag of `BeginAnalysisIndex`"""
        return get_child_object(self.el, "BeginAnalysisIndex", self.tag_dict)

    def BeginSegment(self):
        """Gets the child objects which have short tag of `BeginSegment`, long tag of `BeginSegment`"""
        return get_child_object(self.el, "BeginSegment", self.tag_dict)

    def Column(self):
        """Gets the child objects which have short tag of `Column`, long tag of `Column`"""
        return get_child_object(self.el, "Column", self.tag_dict)

    def EndAnalysisIndex(self):
        """Gets the child objects which have short tag of `EndAnalysisIndex`, long tag of `EndAnalysisIndex`"""
        return get_child_object(self.el, "EndAnalysisIndex", self.tag_dict)

    def EndSegment(self):
        """Gets the child objects which have short tag of `EndSegment`, long tag of `EndSegment`"""
        return get_child_object(self.el, "EndSegment", self.tag_dict)

    def MergesAfter(self):
        """Gets the child objects which have short tag of `MergesAfter`, long tag of `MergesAfter`"""
        return get_child_object(self.el, "MergesAfter", self.tag_dict)

    def MergesBefore(self):
        """Gets the child objects which have short tag of `MergesBefore`, long tag of `MergesBefore`"""
        return get_child_object(self.el, "MergesBefore", self.tag_dict)
