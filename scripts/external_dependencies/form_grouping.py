import math

# Kris's library
# from corpus_toolkit import corpus_tools as ct

from flexpy.Corpus import Corpus
from flexpy.CorpusAnalysis import collocator_separating_target_and_collocate_terms
from flexpy.FormGrouping import (
    group_wordforms,
    group_wordforms_in_text,
    get_form_group_last_morpheme,
    get_form_group_last_morpheme_form,
    get_form_group_last_morpheme_gloss,
    get_form_group_text_only,
)
from flexpy.Text import Text



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
    corpus = Corpus(project_dir, project_name, include_punctuation=False)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    wordform_contents = corpus.get_wordform_contents(
        texts_separated=True,
        paragraphs_separated=False,
        sentences_separated=False,
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
