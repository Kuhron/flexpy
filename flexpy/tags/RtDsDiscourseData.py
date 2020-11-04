from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object

class RtDsDiscourseData(Rt):
    def __init__(self, rt, rt_dict):
        super().__init__(rt, rt_dict)
        self.ChartMarkers = get_child_object(self.rt, "ChartMarkers", self.rt_dict)
        self.Charts = get_child_object(self.rt, "Charts", self.rt_dict)
        self.ConstChartTempl = get_child_object(self.rt, "ConstChartTempl", self.rt_dict)
