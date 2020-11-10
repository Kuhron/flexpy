from flexpy.Corpus import Corpus
from flexpy.Text import Text


def get_form_group_first1(token):
    # first two letters of token
    return token.form[:2]


def get_form_group_last2(token):
    # last two letters of token
    return token.form[-2:]


def get_form_group_pos(token):
    return token.pos


def group_forms_in_corpus(corpus, grouping_function):
    new_corpus = Corpus()
    for text in corpus.texts:
        text = group_forms_in_text(text, grouping_function)
        new_corpus.add_text(text)
    return new_corpus


def group_forms_in_text(text, grouping_function):
    new_text = Text()
    for token in text:
        token = grouping_function(token)
        new_text.add_token(token)
    return new_text


if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)
    # contents = corpus.get_contents()
    for text in corpus.texts:
        print(text)