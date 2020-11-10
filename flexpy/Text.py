from flexpy.FlexPyUtil import get_single_child
from flexpy.TextParagraph import TextParagraph
from flexpy.tags.RtStText import RtStText
from flexpy.tags.RtStTxtPara import RtStTxtPara



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
        text_paragraphs = []
        for st_text in self.st_texts:
            paragraphs_el = st_text.Paragraphs
            rt_st_txt_paras = paragraphs_el.RtStTxtPara
            for rt_st_txt_para in rt_st_txt_paras:
                text_paragraph = TextParagraph(rt_st_txt_para, self.tag_dict)
                text_paragraphs.append(text_paragraph)
        return text_paragraphs

    def create_contents(self):
        # ignores StTexts, treats as flat list of paragraphs
        run_texts = []
        for text_paragraph in self.paragraphs:
            run_texts += text_paragraph.run_texts
        return run_texts
    
    def create_contents_objects(self):
        result = []
        for text_paragraph in self.paragraphs:
            segments = text_paragraph.segments
            print(segments)
            raise NotImplementedError
            # analyses = segments.Analyses
            # print(analyses)
            # gloss_text = analyses.WfiGloss.Form.AUni.text
             #print(gloss_text)
        print("contents objects result for {} is:\n{}".format(self, result))
        return result


    def has_contents(self):
        return self.contents is not None

    def __repr__(self):
        return "<Text name='{}' guid={}>".format(self.name, self.guid)
