from flexpy.tags.RtPunctuationForm import RtPunctuationForm


class PunctuationForm:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def from_rt_punctuation_form(rt_punctuation_form, tag_dict):
        # tag_dict not used right now, but pass it for uniformity with similar methods in other classes,
        # and in case it is needed later
        assert type(rt_punctuation_form) is RtPunctuationForm, rt_punctuation_form
        form = rt_punctuation_form.Form()
        str_tag = form.Str()
        run = str_tag.Run()
        assert len(run) == 1, run
        text = run[0].text
        return PunctuationForm(text)
    
    def is_end_of_sentence(self):
        return self.text in [".", "?", "!", "..."]
    
    def __repr__(self):
        return "<PunctuationForm \"{}\">".format(self.text)