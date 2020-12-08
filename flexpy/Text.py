from flexpy.FlexPyUtil import get_single_child
from flexpy.PunctuationForm import PunctuationForm
from flexpy.TextParagraph import TextParagraph
from flexpy.WordForm import WordForm
from flexpy.tags.RtText import RtText
from flexpy.tags.RtStText import RtStText
from flexpy.tags.RtStTxtPara import RtStTxtPara



class Text:
    def __init__(self, guid, rt, tag_dict, include_punctuation):
        assert type(include_punctuation) is bool
        self.validity = True  # some texts in FLEx are just empty (invalid), not sure why they exist
        self.guid = guid
        assert rt.tag == "rt" and rt.attrib["class"] == "Text"
        self.rt = rt
        self.rt_text = RtText(rt, tag_dict)
        self.tag_dict = tag_dict
        self.include_punctuation = include_punctuation
        self.name = self.create_name()
        self.st_texts = self.create_st_texts()
        self.paragraphs = self.create_paragraphs(self.include_punctuation)
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
        contents = self.rt_text.Contents()
        if contents is None:
            return None
        st_texts = contents.RtStText()
        # elements_owned_by_text = self.tag_dict.get_by_owner_guid(self.guid)
        # st_text_els = [x for x in elements_owned_by_text if x.attrib["class"] == "StText"]
        # st_texts = [RtStText(el, self.tag_dict) for el in st_text_els]
        return st_texts

    def create_paragraphs(self, include_punctuation):
        assert type(include_punctuation) is bool
        # print("creating paragraphs for text {}".format(self))
        text_paragraphs = []
        if self.st_texts is None:
            # print("- no paragraphs found")
            return None
        for st_text_i, st_text in enumerate(self.st_texts):
            # print("StText {}/{}".format(st_text_i, len(self.st_texts)))
            paragraphs_el = st_text.Paragraphs()
            rt_st_txt_paras = paragraphs_el.RtStTxtPara()
            for rt_st_txt_para_i, rt_st_txt_para in enumerate(rt_st_txt_paras):
                # print("RtStTxtPara {}/{}".format(rt_st_txt_para_i, len(rt_st_txt_paras)))
                text_paragraph = TextParagraph(rt_st_txt_para, self.tag_dict, include_punctuation)
                text_paragraphs.append(text_paragraph)
                # print("done with RtStTxtPara {}".format(rt_st_txt_para_i))
        # print("- done creating paragraphs for text {}".format(self))
        return text_paragraphs
    
    def get_wordform_contents(self, paragraphs_separated, sentences_separated):
        assert type(paragraphs_separated) is bool, paragraphs_separated
        assert type(sentences_separated) is bool, sentences_separated
        assert paragraphs_separated ^ sentences_separated, "cannot have both paragraphs and sentences separated"
        if paragraphs_separated:
            contents = []
            for paragraph in self.paragraphs:
                contents.append(paragraph.wordforms)
            return contents
        elif sentences_separated:
            assert self.include_punctuation, "cannot separate sentences in text without punctuation"
            raw_contents = []
            for paragraph in self.paragraphs:
                raw_contents += paragraph.wordforms
            sentences = []
            this_sentence = []
            for wf in raw_contents:
                if type(wf) is PunctuationForm:
                    if wf.is_end_of_sentence():
                        # don't add it, but stop this sentence
                        sentences.append(this_sentence)
                        this_sentence = []  # start a new one
                    else:
                        # it's some other punctuation; omit it
                        continue
                else:
                    assert type(wf) is WordForm
                    this_sentence.append(wf)
            # if somehow we have trailing words at the end without ending punctuation, add those too
            if this_sentence != []:
                sentences.append(this_sentence)
            # get rid of empty-list "sentences" which are created sometimes
            sentences = [x for x in sentences if x != []]
            return sentences
        else:
            contents = []
            for paragraph in self.paragraphs:
                contents += paragraph.wordforms
            return contents

    def create_contents(self):
        # print("creating contents for text {}".format(self))
        # ignores StTexts, treats as flat list of paragraphs
        run_texts = []
        if self.paragraphs is None:
            # print("- no contents found")
            return None
        for text_paragraph in self.paragraphs:
            run_texts += text_paragraph.run_texts
        # print("- done creating contents for text {}".format(self))
        return run_texts
    
    # def create_contents_objects(self):
    #     result = []
    #     for text_paragraph in self.paragraphs:
    #         segments = text_paragraph.segments
    #         print(segments)
    #         raise NotImplementedError
    #         # analyses = segments.Analyses
    #         # print(analyses)
    #         # gloss_text = analyses.WfiGloss.Form.AUni.text
    #          #print(gloss_text)
    #     print("contents objects result for {} is:\n{}".format(self, result))
    #     return result


    def has_contents(self):
        return self.contents is not None

    def __repr__(self):
        return "<Text name='{}' guid={}>".format(self.name, self.guid)
