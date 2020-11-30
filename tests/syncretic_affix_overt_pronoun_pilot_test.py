import math

# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.Corpus import Corpus
from flexpy.CorpusAnalysis import collocator_separating_target_and_collocate_terms
from flexpy.Text import Text


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

    bongu_agreement_affixes_tuples = [
        ("aim", r"2s\.fpst"),
        ("ain", r"3s\.fpst"),
        ("am", r"2s\.ifut"),
        ("an", r"3s\.ifut"),
        ("aq", r"irr.*"),
        ("balan", r"23ns.*"),
        ("ban", r"23ns.*"),
        ("beb", r"23ns.*"),
        ("beben", r"23ns.*"),
        ("ber", r"23ns.*"),
        ("beren", r"23ns.*"),
        ("berlan", r"23d.*"),
        ("bes", r"23ns.*"),
        ("besen", r"23ns.*"),
        ("beslan", r"23d.*"),
        ("buleren", r"23d.*"),
        # "-bun" is not well understood
        ("bus", r"3ns.*"),
        ("busen", r"3ns.*"),
        ("busun", r"3ns.*"),
        ("e", r"2s\.imp"),
        ("eben", r"23ns.*"),
        ("eblan", r"23d.*"),
        ("em", r"2s.*"),
        ("emen", r"1s\.fpst"),  # don't use character class like r"[12]" because then it will think it's syncretic for person (has substr "12")
        ("emen", r"2s\.fut\?"),  # just treat this as a separate suffix from -emen 1s.fpst
        ("emun", r"1ns.*"),
        ("en", r"3s.*"),
        ("eqen", r"3s\.prs\?"),
        ("eren", r"3s.*"),
        ("es", r"3s\.r\.ss"),  # this one is not syncretic
        ("es", r"irr.*"),  # this one IS syncretic, for all person and numbers
        ("esen", r"3s.*"),
        # -esen as different-subject marker is not well understood
        ("ib", r"2ns\.imp"),
        # -im not understood
        ("man", r"1s.*"),
        ("mem", r"1s.*"),
        ("memen", r"1s.*"),
        ("memes", r"12s.*"),
        ("meq", r"2s.*"),
        ("meqen", r"2s.*"),
        ("mere", r"2s.*"),
        ("meren", r"12s.*"),
        ("mes", r"12s.*"),
        ("mesen", r"12s.*"),
        ("mulan", r"1d\.rpst"),
        ("mum", r"1ns.*"),
        ("mun", r"1ns.*"),
        ("mur", r"1ns.*"),
        ("muren", r"1ns.*"),
        ("mus", r"1ns.*"),
        ("musen", r"1ns.*"),
    ]

    has_person_feature = lambda tup: any(x in tup[1] for x in ["1", "2", "3"])
    is_syncretic_for_person = lambda tup: any(x in tup[1] for x in ["12", "23"]) or not has_person_feature(tup)
    is_syncretic_for_number = lambda tup: "ns" in tup[1] or not has_person_feature(tup)  # e.g. irr.ss has no person or number feature, is syncretic to the max
    is_syncretic = lambda tup: is_syncretic_for_person(tup) or is_syncretic_for_number(tup)

    syncretic_affixes_for_person_tuples = [tup for tup in bongu_agreement_affixes_tuples if is_syncretic_for_person(tup)]
    syncretic_affixes_for_number_tuples = [tup for tup in bongu_agreement_affixes_tuples if is_syncretic_for_number(tup)]
    syncretic_affixes = [tup for tup in bongu_agreement_affixes_tuples if is_syncretic(tup)]
    non_syncretic_affixes = [tup for tup in bongu_agreement_affixes_tuples if not is_syncretic(tup)]

    print("syncretic affixes:")
    print(syncretic_affixes)
    print("non-syncretic affixes:")
    print(non_syncretic_affixes)


    # now go through the whole corpus, get any morphemes that match something in the affix list
    for thing in wordform_contents:
        print("I'm a thing in the wordform contents:", thing)
        input("press enter to continue")
    # affixes_matching_morpheme = lambda morpheme: [tup for tup in bongu_agreement_affixes_tuples if ]


    raise
    # target_grouping_function = ?
    collocate_grouping_function = get_form_group_last_morpheme
    corpus_in_target_terms = group_wordforms(wordform_contents, target_grouping_function)
    corpus_in_collocate_terms = group_wordforms(wordform_contents, grouping_function)
    print("\n-- reporting pronoun collocations")
    report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms)
