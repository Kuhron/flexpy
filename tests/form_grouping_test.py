import math

# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.Corpus import Corpus
from flexpy.CorpusAnalysis import collocator_separating_target_and_collocate_terms
from flexpy.Text import Text


def get_form_group_text_only(wordform):
    return wordform.text


def get_form_group_first2(wordform):
    # test function: first two letters of token
    return wordform.text[:2]


def get_form_group_last2(wordform):
    # test function: last two letters of token
    return wordform.text[-2:]


# has problems with some wordforms having more than one root pos, e.g. {"Verb", None}
# this is a problem with how the data is labeled, need to clean up word classes if use this
# def get_form_group_pos(wordform):
#     return wordform.get_root_pos()


def get_form_group_last_morpheme(wordform):
    morph_type = wordform.morph_types[-1]
    form = wordform.forms[-1]
    if form is None:
        return "None"
    elif morph_type in [None, "None"]:
        return "None"
    elif morph_type in ["root", "stem"]:
        form_notation = form
    elif morph_type == "bound root":
        form_notation = "*" + form
    elif morph_type == "suffix":
        form_notation = "-" + form
    elif morph_type == "prefix":
        form_notation = form + "-"
    elif morph_type == "enclitic":
        form_notation = "=" + form
    elif morph_type == "proclitic":
        form_notation = form + "="
    else:
        raise Exception("unknown morph type: {}".format(morph_type))
    gloss = wordform.glosses[-1]
    return "{} ({})".format(form_notation, gloss)


def get_form_group_last_morpheme_form(wordform):
    return wordform.forms[-1]


def get_form_group_last_morpheme_gloss(wordform):
    return wordform.glosses[-1]


def group_wordforms(tokenized, grouping_function):
    new_tokenized = []
    for text in tokenized:
        new_text = group_wordforms_in_text(text, grouping_function)
        new_tokenized.append(new_text)
    return new_tokenized


def group_wordforms_in_text(text, grouping_function):
    new_text = []
    for token in text:
        new_token = grouping_function(token)
        new_text.append(new_token)
    return new_text


def report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms):
    words_of_interest = ["aji", "ni", "andu"]
    metrics = ["MI", "T"]
    for word in words_of_interest:
        for metric in metrics:
            collocates = collocator_separating_target_and_collocate_terms(
                corpus_in_target_terms,
                corpus_in_collocate_terms,
                word, left=4, right=4, stat=metric, cutoff=5, ignore=[]
            )
            print("----\nCollocations for {} using stat={}:".format(word, metric))
            ct.head(collocates, hits=10)


if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    wordform_contents = corpus.get_wordform_contents(
        texts_separated=True,
        paragraphs_separated=False,
        texts_to_omit=texts_to_omit,
    )

    # test grouping functions
    target_grouping_function = get_form_group_text_only
    grouping_functions = [
        # get_form_group_first2,
        # get_form_group_last2,
        get_form_group_last_morpheme,
        # get_form_group_last_morpheme_gloss,
        # get_form_group_last_morpheme_form,
    ]
    for grouping_function in grouping_functions:
        corpus_in_target_terms = group_wordforms(wordform_contents, target_grouping_function)
        corpus_in_collocate_terms = group_wordforms(wordform_contents, grouping_function)
        print("\n-- reporting pronoun collocations")
        report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms)
