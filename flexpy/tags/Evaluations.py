from flexpy.FlexPyUtil import get_child_object

class Evaluations:
    def __init__(self, el, tag_dict):
        self.el = el
        self.RtCmAgentEvaluation = get_child_object(self.el, "rt", self.tag_dict, class_name="CmAgentEvaluation")
