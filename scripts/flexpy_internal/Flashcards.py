import random

from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon


def ask_lex(lex_entries):
    lex = random.choice(lex_entries)
    ask_form_or_gloss = random.choice(["form", "gloss"])
    form = lex.lexeme_form
    glosses = lex.glosses
    if len(glosses) == 0:
        print(f"lex with no gloss: {lex}")
        return
    if ask_form_or_gloss == "form":
        input(f"What does \"{form}\" mean?")
        print(f"\"{form}\" means {glosses}")
    elif ask_form_or_gloss == "gloss":
        rg = random.choice(glosses)
        input(f"How do you say \"{rg}\"?")
        print(f"\"{form}\" means {glosses}")
    else:
        raise


def ask_paragraph(paragraphs):
    p = random.choice(paragraphs)
    ask_form_or_gloss = random.choice(["form", "gloss"])
    form = p.raw_text
    gloss = p.free_translation
    if ask_form_or_gloss == "form":
        input(f"What does \"{form}\" mean?")
        print(f"\"{form}\" means \"{gloss}\"")
    elif ask_form_or_gloss == "gloss":
        input(f"How do you say \"{gloss}\"?")
        print(f"\"{form}\" means \"{gloss}\"")
    else:
        raise


# project_dir = "/home/wesley/uoworkinthefield/FieldMethods/FlexProjectsDir"  # it doesn't seem to work with following symlink
project_dir = "/mnt/c/ProgramData/SIL/FieldWorks/Projects"
project_name = "Ixpantepec Mixtec"
corpus = Corpus(project_dir, project_name, include_punctuation=False)
# contents = corpus.get_tokenized_contents()

lexicon = corpus.lexicon
lex_entries = lexicon.lex_entries
texts = corpus.texts
paragraphs = []
for text in texts:
    if text.paragraphs is not None:
        paragraphs += text.paragraphs
n_lex = len(lex_entries)
n_para = len(paragraphs)
print(f"There are {n_lex} LexEntry objects and {n_para} TextParagraph objects.")
prob_lex = n_lex / (n_lex + n_para)

print("starting quiz\n")
while True:
    if random.random() < prob_lex:
        ask_lex(lex_entries)
    else:
        ask_paragraph(paragraphs)
    input("press enter for the next question")
    print("\n")
