from flexpy.FlexPyUtil import get_single_child

class Text:
    def __init__(self, guid, rt, rt_dict):
        self.guid = guid
        self.rt = rt
        self.rt_dict = rt_dict
        self.name = self.get_name()
        self.contents = self.get_contents()


    def get_name(self):
        try:
            abbreviation = get_single_child(self.rt, "Abbreviation")
            auni = get_single_child(abbreviation, "AUni")
            return auni.text
        except:
            return None


    def get_contents(self):
        # contents_element = self.rt.findall("Contents")
        # print("got contents element: {}".format(contents_element))

        run_texts = []
        # contents_str = ""
        elements_owned_by_text = self.rt_dict.get_by_owner_guid(self.guid)
        # print("elements owned by {} are:\n{}".format(self.guid, elements_owned_by_text))
        st_texts = [x for x in elements_owned_by_text if x.attrib["class"] == "StText"]
        # print("got StTexts: {}".format(st_texts))
        for st_text in st_texts:
            # print("this StText: {}".format(st_text))
            paragraphs = st_text.findall("Paragraphs")
            # print("paragraphs: {}".format(paragraphs))
            for paragraph in paragraphs:
                objsurs = paragraph.findall("objsur")
                if objsurs is None:
                    # print("Warning: paragraph {} has no objsurs".format(paragraph))
                    continue
                for objsur in objsurs:
                    st_text_para_guid = objsur.attrib["guid"]
                    st_text_paragraph = self.rt_dict[st_text_para_guid]
                    contents = get_single_child(st_text_paragraph, "Contents")
                    if contents is None:
                        continue
                    str_element = get_single_child(contents, "Str")
                    # there may be multiple run elements (because of Flex's writing system thing), just concat them
                    run_elements = str_element.findall("Run")
                    run_text = "".join(x.text for x in run_elements)
                    run_texts.append(run_text)
                    # contents_str += run_text
        return run_texts

    def has_contents(self):
        return self.contents is not None

    def __repr__(self):
        return "<Text name='{}' guid={}>".format(self.name, self.guid)
