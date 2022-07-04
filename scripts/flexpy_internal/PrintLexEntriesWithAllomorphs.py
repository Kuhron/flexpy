from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon
import flexpy.FlexPyUtil as util


project_dir = "/home/wesley/.local/share/fieldworks/Projects"
project_name = "IxpantepecMixtec"
lexicon = Lexicon.from_project_dir_and_name(project_dir, project_name)
lex_entries = lexicon.lex_entries

items = []
for lex_entry in lex_entries:
    allomorphs = sorted(set(x.lower() for x in lex_entry.allomorph_forms))
    segment_strs = [util.get_string_without_tone_diacritics(s) for s in allomorphs]
    tone_patterns = [util.get_tone_letters_from_string(s) for s in allomorphs]
    glosses = sorted(set(lex_entry.glosses))
    glosses = ["NoGloss" if g.strip() == "" else g.strip() for g in glosses]
    # poses = sorted(set(lex_entry.parts_of_speech))
    forms = [f"{allomorph} : {segment_str} + {tone_pattern}" for allomorph, segment_str, tone_pattern in zip(allomorphs, segment_strs, tone_patterns)]
    item = [forms, glosses]
    items.append(item)

items = sorted(items, key=lambda item: item[0])

for allomorphs, glosses in items:
    print("Forms: \n" + "\n".join(allomorphs))
    print("Glosses: \n" + "\n".join(glosses))
    # print("Parts of speech: \n" + "\n".join(poses))
    print()

