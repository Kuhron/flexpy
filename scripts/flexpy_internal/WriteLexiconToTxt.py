from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon

project_dir = "/mnt/c/ProgramData/SIL/FieldWorks/Projects"
project_name = "Ixpantepec Mixtec"
corpus = Corpus(project_dir, project_name, include_punctuation=False)
lexicon = corpus.lexicon
lex_entries = lexicon.lex_entries

lines = [f"{lex.lexeme_form} = {'; '.join(lex.glosses)}\n" for lex in lex_entries]
lines = sorted(lines, key=str.casefold)

with open(f"lexicon_{project_name}.txt", "w") as f:
    for l in lines:
        f.write(l)

