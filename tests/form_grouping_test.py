from flexpy.Corpus import Corpus
from flexpy.Text import Text


def get_form_group_first2(token):
    # first two letters of token
    return token.form[:2]


def get_form_group_last2(token):
    # last two letters of token
    return token.form[-2:]


def get_form_group_pos(token):
    return token.pos


def group_forms_in_tokenized(tokenized, grouping_function):
    new_tokenized = []
    for text in tokenized:
        new_text = group_forms_in_tokenized_text(text, grouping_function)
        new_tokenized.append(new_text)
    return new_tokenized


def group_forms_in_tokenized_text(text, grouping_function):
    new_text = []
    for token in text:
        new_token = grouping_function(token)
        new_text.append(new_token)
    return new_text


def report_pronoun_collocations(tokenized):
    words_of_interest = ["aji", "ni", "andu"]
    metrics = ["MI", "T"]
    for word in words_of_interest:
        for metric in metrics:
            collocates = ct.collocator(tokenized, word, stat=metric)
            print("----\nCollocations for {} using stat={}:".format(word, metric))
            ct.head(collocates, hits=10)


if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)
    print("\n-- all texts in corpus:")
    for text in corpus.texts:
        print(text)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    # tokenized = corpus.get_tokenized_contents_objects(texts_to_omit=texts_to_omit)

    # test grouping functions
    # for grouping_function in [get_form_group_first2, get_form_group_last2, get_form_group_pos]:
    #     new_tokenized = group_forms_in_tokenized(tokenized, grouping_function)
    #     print("\n-- reporting pronoun collocations")
    #     report_pronoun_collocations(new_tokenized)
