from flexpy.FlexPyUtil import get_single_child
from flexpy.TextParagraph import TextParagraph



class Text:
    def __init__(self, guid, rt, rt_dict):
        self.validity = True  # some texts in FLEx are just empty (invalid), not sure why they exist
        self.guid = guid
        self.rt = rt
        self.rt_dict = rt_dict
        self.name = self.get_name()
        self.contents = self.get_contents()

    def is_valid(self):
        assert type(self.validity) is bool
        return self.validity

    def get_name(self):
        abbreviation = get_single_child(self.rt, "Abbreviation")
        if abbreviation is None:
            self.validity = False
            if self.rt.find("Contents") is not None:
                pass #raise Exception("Text found with contents but no name, in rt element: {}, guid {}".format(self.rt, self.rt.attrib["guid"]))
            return None
        else:
            auni = get_single_child(abbreviation, "AUni")
            return auni.text

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
                    st_text_para_el = self.rt_dict[st_text_para_guid]
                    text_paragraph = TextParagraph(st_text_para_el, self.rt_dict)
                    run_texts += text_paragraph.run_texts
        return run_texts

    def has_contents(self):
        return self.contents is not None

    def __repr__(self):
        return "<Text name='{}' guid={}>".format(self.name, self.guid)
