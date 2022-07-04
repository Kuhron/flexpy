import xml.etree.ElementTree as ET
from flexpy.FlexPyUtil import get_single_child, get_str_from_AStrs
from flexpy.PunctuationForm import PunctuationForm
from flexpy.TagDict import TagDict
from flexpy.WordForm import WordForm

from flexpy.tags.RtPunctuationForm import RtPunctuationForm
from flexpy.tags.RtSegment import RtSegment
from flexpy.tags.RtStTxtPara import RtStTxtPara
from flexpy.tags.RtWfiAnalysis import RtWfiAnalysis
from flexpy.tags.RtWfiGloss import RtWfiGloss



class TextParagraph:
    """A FlexPy-specific class for holding the information in a single "TextParagraph"
    in FLEx. Texts are composed of a list of such paragraphs.

    :param rt_st_txt_para: The `rt` element with class_name `StTxtPara` in FLEx
    :type rt_st_txt_para: xml.etree.ElementTree.Element
    :param tag_dict:
    :type tag_dict: TagDict
    :param include_punctuation:
    :type include_punctuation: bool
    """
    def __init__(self, rt_st_txt_para, tag_dict, include_punctuation):
        assert type(rt_st_txt_para) is RtStTxtPara, type(rt_st_txt_para)
        assert type(tag_dict) is TagDict
        assert type(include_punctuation) is bool
        self.rt_st_txt_para = rt_st_txt_para
        self.tag_dict = tag_dict
        self.include_punctuation = include_punctuation
        self.run_texts = self.create_run_texts()
        self.wordforms = self.create_wordforms(include_punctuation=self.include_punctuation)
        self.raw_text = self.get_raw_text()
        self.free_translation = self.get_free_translation()
    
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
                run_text = "".join(x.text if x.text is not None else "" for x in run)
            else:
                run_text = run.text
            run_texts.append(run_text)
        return run_texts
    
    def get_raw_text(self):
        return "".join(self.run_texts)
    
    def create_wordforms(self, include_punctuation):
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
            if analyses is None:
                # print("analyses is None")
                continue
            # print("Analyses has these child objects: {}".format(analyses.get_ordered_child_objects()))
            for child_obj in analyses.get_ordered_child_objects():
                if type(child_obj) is RtWfiAnalysis:
                    wordform = WordForm.from_rt_wfi_analysis(child_obj, self.tag_dict)
                elif type(child_obj) is RtWfiGloss:
                    wordform = WordForm.from_rt_wfi_gloss(child_obj, self.tag_dict)
                elif include_punctuation and type(child_obj) is RtPunctuationForm:
                    wordform = PunctuationForm.from_rt_punctuation_form(child_obj, self.tag_dict)
                    # varname "wordform" misleading in this case, but keeping just so it is appended like usual
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

    def get_free_translation(self):
        segments = self.rt_st_txt_para.Segments()
        if segments is None:
            return None
        rt_segments = segments.RtSegment()
        s = ""
        for rt_segment in rt_segments:
            free_translation = rt_segment.FreeTranslation()
            if free_translation is not None:
                astrs = free_translation.AStr()
                this_s = get_str_from_AStrs(astrs)
                s += this_s
        return s
