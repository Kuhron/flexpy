import xml.etree.ElementTree as ET
from flexpy.FlexPyUtil import get_single_child
from flexpy.TagDict import TagDict
from flexpy.WordForm import WordForm

from flexpy.tags.RtSegment import RtSegment
from flexpy.tags.RtStTxtPara import RtStTxtPara


class TextParagraph:
    def __init__(self, rt_st_txt_para, tag_dict):
        assert type(rt_st_txt_para) is RtStTxtPara, type(rt_st_txt_para)
        assert type(tag_dict) is TagDict
        self.rt_st_txt_para = rt_st_txt_para
        self.tag_dict = tag_dict
        self.run_texts = self.create_run_texts()
        self.segments = self.create_segments()

    def create_run_texts(self):
        run_texts = []
        contents = self.rt_st_txt_para.Contents
        if contents is not None:
            str_obj = contents.Str
            # there may be multiple run elements (because of Flex's writing system thing), just concat them
            run = str_obj.Run
            if type(run) is list:
                run_text = "".join(x.text for x in run)
            else:
                run_text = run.text
            run_texts.append(run_text)
        return run_texts
    
    def create_segments(self):
        result = []
        rt_segments = self.rt_st_txt_para.Segments.RtSegment  # should be list because of objsurs
        for rt_segment in rt_segments:
            assert type(rt_segment) is RtSegment, type(rt_segment)
            print("rt segment: {}".format(rt_segment))
            analyses = rt_segment.Analyses
        print(analyses)
        print(analyses.RtPunctuationForm)
        print(analyses.RtWfiAnalysis)
        print(analyses.RtWfiGloss)
        print(analyses.RtWfiWordform)
        gloss_owner_els = [x.owner_el for x in analyses.RtWfiGloss]
        print(gloss_owner_els)
        gloss_owners = [self.tag_dict.get_python_object_from_element(el) for el in gloss_owner_els]
        print(gloss_owners)
        wordforms = [WordForm(wfi_analysis, self.tag_dict) for wfi_analysis in gloss_owners]
        print(wordforms)
        input("^")