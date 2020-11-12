import os
import random

from flexpy.Lexicon import Lexicon
from flexpy.TagDict import TagDict
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
        self.tag_dict = self.get_tag_dict()
        self.texts = self.get_texts()
        self.lexicon = self.get_lexicon()

    def get_tag_dict(self):
        return TagDict.from_project_dir_and_name(self.project_dir, self.project_name)

    def get_texts(self):
        text_elements = self.tag_dict["RtText"]
        texts = []
        for guid, rt in text_elements.items():
            # print("initing new text from rt {}".format(rt))
            text = Text(guid, rt, self.tag_dict)
            # print("finished initing text {}".format(text))
            texts.append(text)
        # print("there are {} texts with contents".format(sum(x.has_contents() for x in texts)))
        return texts

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

    def get_contents(self, texts_to_omit=None):
        # e.g. ["Hello, world.", "My name is Wesley."]
        if texts_to_omit is None and hasattr(self, "contents"):
            return self.contents
        contents_lst = []
        for text in self.texts:
            if texts_to_omit is not None and text.name in texts_to_omit:
                continue
            contents = text.contents
            contents_lst += contents
        return contents_lst

    def get_tokenized_contents(self, texts_to_omit=None):
        # e.g. [["hello", "world"], ["my", "name", "is", "wesley"]]
        contents = self.get_contents(texts_to_omit=texts_to_omit)
        result = []
        for s in self.contents:
            result.append(tokenize_single_text(s))
        return result

    def get_tokenized_contents_flat(self):
        # treats the whole corpus as a single text
        # e.g. ["hello", "world", "my", "name", "is", "wesley"]
        contents = self.get_contents(texts_to_omit=texts_to_omit)
        result = []
        for s in contents:
            result += tokenize_single_text(s)
        return result
    
    def get_tokenized_contents_objects(self, texts_to_omit=None):
        result = []
        for text in self.texts:
            if texts_to_omit is not None and text.name in texts_to_omit:
                print("text {} is omitted".format(text.name))
                continue
            result.append(text.create_contents_objects())
        return result

    def get_lexicon(self):
        lex_entries = self.tag_dict["RtLexEntry"]
        return Lexicon(lex_entries, self.tag_dict)

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
