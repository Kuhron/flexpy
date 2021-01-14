# implementation of methods from Hammarström's 2019 presentation
# "Prospects for a (Semi-)Automated Papuan Comparative Linguistics and Reconstruction"

import os
from flexpy.Corpus import Corpus


class LexiconSimple:
    def __init__(self, lexemes):
        self.lexemes = lexemes


class LexemeSimple:
    def __init__(self, form, poses, glosses):
        self.form = form
        self.poses = poses
        self.glosses = glosses


def load_lexicon_from_tsv(fp):
    print("loading tsv for lexicon of {}".format(ln))
    with open(fp) as f:
        lines = f.readlines()
    lexemes = []
    for line in lines:
        form, pos_csv, gloss_csv = line.split("\t")
        poses = pos_csv.split(",")
        glosses = gloss_csv.split(",")
        lexeme = LexemeSimple(form, poses, glosses)
        lexemes.append(lexeme)
    lexicon = LexiconSimple(lexemes)
    return lexicon


def write_lexicon_tsv(corpus, fp):
    lexicon = corpus.lexicon
    lexicons[ln] = lexicon
    lex_entries = lexicon.lex_entries
    s = ""
    for lex_entry in lex_entries:
        s += lex_entry.tsv_repr() + "\n"
    with open(fp, "w") as f:
        f.write(s)


if __name__ == "__main__":
    language_names = [
        # wesley@lumen:~/.local/share/fieldworks/Projects$ ls | xargs -d "\t" echo | sed -e "s/^/\"/g" | sed -e "s/$/\",/g"
        # "Acoma",  # not Papuan!
        "Aisi Mabɨŋ",
        "Aisi Magɨ",
        "Bara",
        "Bere",
        "Bongu",
        # "dnw-flex",  # not Madang
        "Gants",  # problem with multiple lexeme forms
        # "Isan",  # not Papuan!
        "Kursav",
        "Manat",
        "Mand",
        "Sa",
        "Sirva",
        "Soq",
        # "test",
        "Yangulam",
    ]
    print("found {} languages".format(len(language_names)))
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    lexicons = {}
    wordlist_dir = "/home/wesley/flexpy/flexpy/language_data/MadangWordlists/"
    for ln in language_names:
        print("-- loading language {}".format(ln))
        filename = "{}.tsv".format(ln)
        fp = os.path.join(wordlist_dir, filename)
        if os.path.exists(fp):
            lexicon = load_lexicon_from_tsv(fp)
            lexicons[ln] = lexicon
        else:
            print("creating tsv for lexicon of {}".format(ln))
            corpus = Corpus(project_dir, ln, include_punctuation=False)
            write_lexicon_tsv(corpus, fp)
            assert os.path.exists(fp)  # should be there now that we wrote it
            lexicon = load_lexicon_from_tsv(fp)
            lexicons[ln] = lexicon

        print("{} has {} lexeme entries".format(ln, len(lexicon.lexemes)))

