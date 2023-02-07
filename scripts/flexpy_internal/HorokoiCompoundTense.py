# for historical syntax project
# find all things that look like the Horokoi compound tense cx (use regex to find them)
# dump them to Excel sheet
# include baseline, free translation, gloss?, text name, line number

import re

from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon
from flexpy.Text import Text


project_dir = "/home/wesley/Horokoi/FLEx/"
project_name = "Horokoi"
corpus = Corpus(project_dir, project_name, include_punctuation=False)
texts = corpus.texts

pattern = r"(khu|mai|mu|p[uia]|mana|ne|p[iu]n?[ae])[^\w]*?kha[iw]"

matching_paragraphs = []
for text in texts:
    for pg in text.paragraphs:
        s = pg.raw_text
        matches = re.search(pattern, s, flags=re.IGNORECASE)
        if matches is not None:
            baseline = pg.raw_text
            translation = pg.free_translation
            text_abbr = text.abbreviation
            line_number = pg.paragraph_number
            location = f"{text_abbr} {line_number}"
            tup = (location, baseline, translation)
            matching_paragraphs.append(tup)

output_fp = "HorokoiCompoundTenseExamplesRaw.tsv"
with open(output_fp, "w") as f:
    for tup in matching_paragraphs:
        f.write("\t".join(tup) + "\n")
print(f"written to {output_fp}")
