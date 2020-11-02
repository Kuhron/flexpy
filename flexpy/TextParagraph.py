# replicating structure of <rt class="StTxtPara">

from flexpy.FlexPyUtil import get_single_child


class TextParagraph:
    def __init__(self, rt, rt_dict):
        self.rt = rt
        self.rt_dict = rt_dict
        self.populate_child_variables()

    def populate_child_variables(self):
        self.run_texts = []
        contents_el = get_single_child(self.rt, "Contents")
        if contents_el is not None:
            str_el = get_single_child(contents_el, "Str")
            # there may be multiple run elements (because of Flex's writing system thing), just concat them
            run_els = str_el.findall("Run")
            run_text = "".join(x.text for x in run_els)
            self.run_texts.append(run_text)

        self.parse_is_current = get_single_child(self.rt, "ParseIsCurrent").attrib["val"]

        self.segments = []
        segments_el = get_single_child(self.rt, "Segments")
        if segments_el is not None:
            objsurs = segments_el.findall("objsur")
            for objsur in objsurs:
                segment_el = self.rt_dict[objsur.attrib["guid"]]

