from flexpy.tags.Rt import Rt
from flexpy.FlexPyUtil import camel_case_to_snake_case


class CmAgent(Rt):
    def __init__(self, el, rt_dict):
        super().__init__(el, rt_dict)
        self.populate_child_variables()

    def populate_child_variables(self):
        for child_el in self.rt:
            tag = child_el.tag
            attr_name = camel_case_to_snake_case(tag)
            print(tag, attr_name)
            input()
