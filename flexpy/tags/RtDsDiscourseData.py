from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtDsDiscourseData(Rt):
    def __init__(self, el, tag_dict):
        super().__init__(el, tag_dict)
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.ChartMarkers = get_child_object(self.el, "ChartMarkers", self.tag_dict)
        self.Charts = get_child_object(self.el, "Charts", self.tag_dict)
        self.ConstChartTempl = get_child_object(self.el, "ConstChartTempl", self.tag_dict)
