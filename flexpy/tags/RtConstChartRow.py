from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtConstChartRow(Rt):
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

    def Cells(self):
        """Gets the child objects which have short tag of `Cells`, long tag of `Cells`"""
        return get_child_object(self.el, "Cells", self.tag_dict)

    def ClauseType(self):
        """Gets the child objects which have short tag of `ClauseType`, long tag of `ClauseType`"""
        return get_child_object(self.el, "ClauseType", self.tag_dict)

    def EndDependentClauseGroup(self):
        """Gets the child objects which have short tag of `EndDependentClauseGroup`, long tag of `EndDependentClauseGroup`"""
        return get_child_object(self.el, "EndDependentClauseGroup", self.tag_dict)

    def EndParagraph(self):
        """Gets the child objects which have short tag of `EndParagraph`, long tag of `EndParagraph`"""
        return get_child_object(self.el, "EndParagraph", self.tag_dict)

    def EndSentence(self):
        """Gets the child objects which have short tag of `EndSentence`, long tag of `EndSentence`"""
        return get_child_object(self.el, "EndSentence", self.tag_dict)

    def Label(self):
        """Gets the child objects which have short tag of `Label`, long tag of `Label`"""
        return get_child_object(self.el, "Label", self.tag_dict)

    def StartDependentClauseGroup(self):
        """Gets the child objects which have short tag of `StartDependentClauseGroup`, long tag of `StartDependentClauseGroup`"""
        return get_child_object(self.el, "StartDependentClauseGroup", self.tag_dict)
