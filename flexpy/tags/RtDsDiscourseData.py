from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtDsDiscourseData(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        return get_ordered_child_objects(self.el, self.tag_dict)

    def ChartMarkers(self):
        return get_child_object(self.el, "ChartMarkers", self.tag_dict)

    def Charts(self):
        return get_child_object(self.el, "Charts", self.tag_dict)

    def ConstChartTempl(self):
        return get_child_object(self.el, "ConstChartTempl", self.tag_dict)
