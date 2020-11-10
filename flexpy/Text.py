from flexpy.FlexPyUtil import get_single_child
from flexpy.TextParagraph import TextParagraph
from flexpy.tags.RtStText import RtStText



class Text:
    def __init__(self, guid, rt, tag_dict):
        self.validity = True  # some texts in FLEx are just empty (invalid), not sure why they exist
        self.guid = guid
        self.rt = rt
        self.tag_dict = tag_dict
        self.name = self.create_name()
        self.st_texts = self.create_st_texts()
        self.paragraphs = self.create_paragraphs()
        self.contents = self.create_contents()

    def is_valid(self):
        assert type(self.validity) is bool
        return self.validity

    def create_name(self):
        abbreviation = get_single_child(self.rt, "Abbreviation")
        if abbreviation is None:
            self.validity = False
            if self.rt.find("Contents") is not None:
                pass #raise Exception("Text found with contents but no name, in rt element: {}, guid {}".format(self.rt, self.rt.attrib["guid"]))
            return None
        else:
            auni = get_single_child(abbreviation, "AUni")
            return auni.text

    def create_st_texts(self):
        elements_owned_by_text = self.tag_dict.get_by_owner_guid(self.guid)
        st_text_els = [x for x in elements_owned_by_text if x.attrib["class"] == "StText"]
        st_texts = [RtStText(el, self.tag_dict) for el in st_text_els]
        return st_texts

    def create_paragraphs(self):
        paragraphs = []
        for st_text in self.st_texts:
            paragraphs_el = st_text.Paragraphs
            rt_st_text_para_els = paragraphs_el.RtStTxtPara
            paragraphs.append(rt_st_text_para_els)
        return paragraphs

    def create_contents(self):
        # ignores StTexts, treats as flat list of paragraphs
        run_texts = []
        for rt_st_text_para_els in self.paragraphs:
            for rt_st_text_para_el in rt_st_text_para_els:
                text_paragraph = TextParagraph(rt_st_text_para_el, self.tag_dict)
                run_texts += text_paragraph.run_texts
        return run_texts

    def has_contents(self):
        return self.contents is not None

    def __repr__(self):
        return "<Text name='{}' guid={}>".format(self.name, self.guid)
