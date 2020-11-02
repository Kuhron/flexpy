import os

from flexpy.Lexicon import Lexicon
from flexpy.RtDict import RtDict
from flexpy.Text import Text

from flexpy.FlexPyUtil import tokenize_single_text



class Corpus:
    def __init__(self, project_dir, project_name):
        self.project_dir = project_dir
        self.project_name = project_name
        self.rt_dict = self.get_rt_dict()
        self.texts = self.get_texts()
        self.contents = self.get_contents()
        self.lexicon = self.get_lexicon()

    def get_rt_dict(self):
        flex_dir = self.project_dir + "{}/".format(self.project_name)
        fp = flex_dir + "{}.fwdata".format(self.project_name)
        # print("getting corpus from FLEx project {} at {}".format(self.project_name, fp))
        rt_dict = RtDict.from_fwdata_file(fp)
        return rt_dict

    def get_texts(self):
        return self.rt_dict.get_texts()

    def get_valid_texts(self):
        return [x for x in self.get_texts() if x.is_valid()]

    def write_texts_to_file(self, output_dir):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        texts = self.get_valid_texts()
        text_names = [text.name for text in texts]
        assert len(set(text_names)) == len(text_names), "repeat text names found: {}".format(text_names)
        for text in texts:
            filename = "{}.txt".format(text.name)
            output_fp = os.path.join(output_dir, filename)
            with open(output_fp, "w") as f:
                for line in text.contents:
                    f.write(line + "\n")

    def get_contents(self):
        contents_lst = []
        for text in self.texts:
            # print("----")
            # print(text)
            contents = text.get_contents()
            # print(contents)
            contents_lst += contents
            # print("----\n")
        return contents_lst

    def get_tokenized_contents(self):
        # treats the whole corpus as a single text for now
        result = []
        for s in self.contents:
            result += tokenize_single_text(s)
        return result

    def get_lexicon(self):
        lex_entries = self.rt_dict["LexEntry"]
        return Lexicon(lex_entries, self.rt_dict)

    def search_lexicon_glosses(self, regex):
        return self.lexicon.search_glosses(regex)

    def search_word_glosses(self, regex):
        return None

    def search_free_translations(self, regex):
        return None
