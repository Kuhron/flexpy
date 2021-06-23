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
    """A class that contains the lexicon and texts from the FLEx database.

    :param project_dir: the directory where the FLEx project's directory is found
    :type project_dir: str
    :param project_name: the project name (a folder with this name should be inside project_dir)
    :type project_name: str
    :param include_punctuation: whether punctuation tokens should be included
    :type include_punctuation: bool
    """
    def __init__(self, project_dir, project_name, include_punctuation):
        assert type(include_punctuation) is bool
        self.project_dir = project_dir
        self.project_name = project_name
        self.include_punctuation = include_punctuation
        self.tag_dict = self.get_tag_dict()
        self.texts = self.get_texts(self.include_punctuation)
        self.lexicon = self.get_lexicon()

    def get_tag_dict(self):
        """Gets a :class:`flexpy.TagDict.TagDict` object for this project
        """
        return TagDict.from_project_dir_and_name(self.project_dir, self.project_name)

    def get_texts(self, include_punctuation=None):
        """Gets the texts for this project as a list of :class:`flexpy.Text.Text` objects

        :param include_punctuation: 
            whether the texts should contain punctuation tokens 
            (defaults to self.include_punctuation)
        """
        if include_punctuation is None:
            include_punctuation = self.include_punctuation  # you can't have arg=self.arg in the signature bc self is not in scope there
        text_elements = self.tag_dict["RtText"]
        texts = []
        for guid, rt in text_elements.items():
            # print("initing new text from rt {}".format(rt))
            text = Text(guid, rt, self.tag_dict, include_punctuation)
            # print("finished initing text {}".format(text))
            texts.append(text)
        # print("there are {} texts with contents".format(sum(x.has_contents() for x in texts)))
        return texts

    def get_valid_texts(self):
        """Gets the texts which are valid (e.g. non-empty)
        """
        return [x for x in self.get_texts() if x.is_valid()]

    # TODO add exporting to CONLLU, other useful formats.

    def write_texts_to_file(self, output_dir):
        """Writes each text to a separate .txt file in `output_dir`
        """
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        texts = self.get_valid_texts()
        text_names = [text.name for text in texts]
        assert len(set(text_names)) == len(text_names), "repeat text names found: {}".format(text_names)
        for text in texts:
            text_name = text.name.replace("/","_").replace(" ","_")  # prevent filename problems
            filename = "{}.txt".format(text_name)
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
            if contents is not None:
                contents_lst += contents
        return contents_lst

    def get_tokenized_contents(self, texts_to_omit=None):
        """Returns a list of the texts, each of which is a list of string tokens.
        
        e.g. [["hello", "world"], ["my", "name", "is", "wesley"]]
        """
        contents = self.get_contents(texts_to_omit=texts_to_omit)
        result = []
        for s in contents:
            result.append(tokenize_single_text(s))  # tokenize_single_text returns list e.g. ["hello", "world"]
        return result

    def get_tokenized_contents_flat(self, texts_to_omit=None):
        """Returns the texts' contents, treating the whole corpus as a single text.
        
        e.g. ["hello", "world", "my", "name", "is", "wesley"]
        """
        contents = self.get_contents(texts_to_omit=texts_to_omit)
        result = []
        for s in contents:
            result += tokenize_single_text(s)  # tokenize_single_text returns list e.g. ["hello", "world"]
        return result
    
    def get_tokenized_contents_objects(self, texts_to_omit=None):
        result = []
        for text in self.texts:
            if texts_to_omit is not None and text.name in texts_to_omit:
                print("text {} is omitted".format(text.name))
                continue
            result.append(text.create_contents_objects())
        return result

    def get_wordform_contents(self, texts_separated, paragraphs_separated, sentences_separated,
            texts_to_include=None, texts_to_omit=None,
        ):
        assert type(texts_separated) is bool, texts_separated
        assert type(paragraphs_separated) is bool, paragraphs_separated
        assert type(sentences_separated) is bool, sentences_separated
        if texts_to_include is not None and texts_to_omit is not None:
            intersection = set(texts_to_include) & set(texts_to_omit)
            assert intersection == set(), "these texts were listed as both include and omit: {}".format(sorted(intersection))
        if sentences_separated:
            assert self.include_punctuation, "cannot separate sentences in corpus which does not have punctuation included in texts; you must re-initialize the Corpus with include_punctuation=True"

        contents = []
        for text in self.texts:
            valid = text.is_valid()
            included = texts_to_include is None or text.name in texts_to_include
            omitted = texts_to_omit is None or text.name in texts_to_omit
            if valid and included and (not omitted):
                text_contents = text.get_wordform_contents(
                    paragraphs_separated=paragraphs_separated,
                    sentences_separated=sentences_separated,
                )
                if texts_separated:
                    contents.append(text_contents)
                else:
                    print("Warning: getting corpus contents should probably have texts separated as True")
                    contents += text_contents
        return contents

    def get_lexicon(self):
        """Returns a :class:`flexpy.Lexicon.Lexicon` object containing the lexeme entries in this corpus
        """
        lex_entries = self.tag_dict["RtLexEntry"]
        return Lexicon(lex_entries, self.tag_dict)

    def search_lexicon_glosses(self, regex):
        """Searches the glosses of the corpus's lexicon by regex
        """
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
