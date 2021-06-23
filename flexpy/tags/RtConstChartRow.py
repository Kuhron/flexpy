from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtConstChartRow(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Cells(self):
        return get_child_object(self.el, "Cells", self.tag_dict)

    def ClauseType(self):
        return get_child_object(self.el, "ClauseType", self.tag_dict)

    def EndDependentClauseGroup(self):
        return get_child_object(self.el, "EndDependentClauseGroup", self.tag_dict)

    def EndParagraph(self):
        return get_child_object(self.el, "EndParagraph", self.tag_dict)

    def EndSentence(self):
        return get_child_object(self.el, "EndSentence", self.tag_dict)

    def Label(self):
        return get_child_object(self.el, "Label", self.tag_dict)

    def StartDependentClauseGroup(self):
        return get_child_object(self.el, "StartDependentClauseGroup", self.tag_dict)
