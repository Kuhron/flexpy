import xml.etree.ElementTree as ET
from flexpy.FlexPyUtil import get_single_child
from flexpy.TagDict import TagDict
from flexpy.WordForm import WordForm

from flexpy.tags.RtSegment import RtSegment
from flexpy.tags.RtStTxtPara import RtStTxtPara
from flexpy.tags.RtWfiAnalysis import RtWfiAnalysis
from flexpy.tags.RtWfiGloss import RtWfiGloss



class TextParagraph:
    def __init__(self, rt_st_txt_para, tag_dict):
        assert type(rt_st_txt_para) is RtStTxtPara, type(rt_st_txt_para)
        assert type(tag_dict) is TagDict
        self.rt_st_txt_para = rt_st_txt_para
        self.tag_dict = tag_dict
        self.run_texts = self.create_run_texts()
        self.wordforms = self.create_wordforms()
    
    def __repr__(self):
        return "<TextParagraph \"{}\" from rt {}>".format(self.get_raw_text(), self.rt_st_txt_para)

    def create_run_texts(self):
        run_texts = []
        contents = self.rt_st_txt_para.Contents()
        if contents is not None:
            str_obj = contents.Str()
            # there may be multiple run elements (because of Flex's writing system thing), just concat them
            run = str_obj.Run()
            if type(run) is list:
                run_text = "".join(x.text for x in run)
            else:
                run_text = run.text
            run_texts.append(run_text)
        return run_texts
    
    def get_raw_text(self):
        return " ".join(self.run_texts)
    
    def create_wordforms(self):
        # print("creating wordforms for {}".format(self))
        result = []
        segments = self.rt_st_txt_para.Segments()
        if segments is None:
            return []
        rt_segments = segments.RtSegment()  # should be list because of objsurs
        wordforms = []
        for rt_segment_i, rt_segment in enumerate(rt_segments):
            # print("segment {}/{}".format(rt_segment_i, len(rt_segments)))
            assert type(rt_segment) is RtSegment, type(rt_segment)
            analyses = rt_segment.Analyses()
            # print("Analyses has these child objects: {}".format(analyses.get_ordered_child_objects()))
            for child_obj in analyses.get_ordered_child_objects():
                if type(child_obj) is RtWfiAnalysis:
                    wordform = WordForm.from_rt_wfi_analysis(child_obj, self.tag_dict)
                elif type(child_obj) is RtWfiGloss:
                    wordform = WordForm.from_rt_wfi_gloss(child_obj, self.tag_dict)
                else:
                    # print("not making wordform from child {}".format(child_obj))
                    continue  # don't append the wordform var from previous loop iteration

                if wordform is not None:
                    wordforms.append(wordform)

            # OLD stuff by might help showing how to get owner object for accessing other info
            # gloss_owners = [x.get_owner() for x in analyses.RtWfiGloss]
            # # print("gloss owners:", gloss_owners)
            # analysis_owners = [wfi_analysis.get_owner() for wfi_analysis in gloss_owners]
        # print("wordforms:\n- {}".format("\n- ".join(repr(x) for x in wordforms)))
        # input("check")
        # print("- done creating wordforms for {}".format(self))
        return wordforms