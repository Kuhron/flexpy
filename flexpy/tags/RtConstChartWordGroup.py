from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtConstChartWordGroup(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def BeginAnalysisIndex(self):
        return get_child_object(self.el, "BeginAnalysisIndex", self.tag_dict)

    def BeginSegment(self):
        return get_child_object(self.el, "BeginSegment", self.tag_dict)

    def Column(self):
        return get_child_object(self.el, "Column", self.tag_dict)

    def EndAnalysisIndex(self):
        return get_child_object(self.el, "EndAnalysisIndex", self.tag_dict)

    def EndSegment(self):
        return get_child_object(self.el, "EndSegment", self.tag_dict)

    def MergesAfter(self):
        return get_child_object(self.el, "MergesAfter", self.tag_dict)

    def MergesBefore(self):
        return get_child_object(self.el, "MergesBefore", self.tag_dict)
