import os
import random

from flexpy.Lexicon import Lexicon
from flexpy.RtDict import RtDict
from flexpy.Text import Text

from flexpy.FlexPyUtil import (
    print_concordance_pretty,
    sort_concordance_list,
    tokenize_single_text,
)



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
        # e.g. ["Hello, world.", "My name is Wesley."]
        contents_lst = []
        for text in self.texts:
            contents = text.get_contents()
            contents_lst += contents
        return contents_lst

    def get_tokenized_contents(self):
        # e.g. [["hello", "world"], ["my", "name", "is", "wesley"]]
        result = []
        for s in self.contents:
            result.append(tokenize_single_text(s))
        return result

    def get_tokenized_contents_flat(self):
        # treats the whole corpus as a single text
        # e.g. ["hello", "world", "my", "name", "is", "wesley"]
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
        raise NotImplementedError
        return None

    def search_free_translations(self, regex):
        raise NotImplementedError
        return None

    def print_concordance(self, token, sample_size, sorting_indices=None):
        # sample size is how many lines to show
        # sorting indices is a list of indices on which to sort; the indices are number of words away from the token (so zero is the token, -1 is the word before, etc.) and in order of priority
        texts = self.get_tokenized_contents()
        lines_containing_token = [x for x in texts if token in x]
        sample = random.sample(lines_containing_token, min(sample_size, len(lines_containing_token)))
        conc_list = []  # left, target, right for each token
        for line in sample:
            # if it's in there more than once, choose a random one
            token_indices = [i for i, x in enumerate(line) if x == token]
            t_i = random.choice(token_indices)  # will still work if len 1
            left = line[:t_i]
            target = token
            right = line[t_i+1:]
            sub_lst = [left, target, right]
            conc_list.append(sub_lst)

        # sorting
        if sorting_indices is not None:
            conc_list = sort_concordance_list(conc_list, sorting_indices)
        print_concordance_pretty(conc_list, max_words_left=5, max_words_right=5)
