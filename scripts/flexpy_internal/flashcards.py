import random

from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon


# project_dir = "/home/wesley/uoworkinthefield/FieldMethods/FlexProjectsDir"  # it doesn't seem to work with following symlink
project_dir = "/mnt/c/ProgramData/SIL/FieldWorks/Projects"
project_name = "Ixpantepec Mixtec"
corpus = Corpus(project_dir, project_name, include_punctuation=False)
# contents = corpus.get_tokenized_contents()

lexicon = corpus.lexicon
lex_entries = lexicon.lex_entries
print(f"There are {len(lex_entries)} LexEntry objects.")

print("starting quiz\n")
while True:
    lex = random.choice(lex_entries)
    ask_form_or_gloss = random.choice(["form", "gloss"])
    form = lex.lexeme_form
    glosses = lex.glosses
    if len(glosses) == 0:
        continue
    if ask_form_or_gloss == "form":
        input(f"What does \"{form}\" mean?")
        print(f"\"{form}\" means {glosses}")
    elif ask_form_or_gloss == "gloss":
        rg = random.choice(glosses)
        input(f"How do you say \"{rg}\"?")
        print(f"\"{form}\" means {glosses}")
    else:
        raise
    input("press enter for the next question")
    print("\n")
