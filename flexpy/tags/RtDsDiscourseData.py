from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtDsDiscourseData(Rt):
    def __init__(self, rt, tag_dict):
        super().__init__(rt, tag_dict)
        self.ChartMarkers = get_child_object(self.rt, "ChartMarkers", self.tag_dict)
        self.Charts = get_child_object(self.rt, "Charts", self.tag_dict)
        self.ConstChartTempl = get_child_object(self.rt, "ConstChartTempl", self.tag_dict)
