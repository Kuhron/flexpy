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

pattern = r"(khu|mai|mu|p[uia]|mana|ne|p[iu]n?[ae])[^\w]*?kha[iw]"
output_fp = "HorokoiCompoundTenseExamplesRaw.tsv"
corpus.write_paragraphs_matching_regex(pattern, output_fp)
