# for historical syntax project
# find all things that look like the Horokoi compound tense cx (use regex to find them)
# dump them to Excel sheet
# include baseline, free translation, gloss?, text name, line number

import os
import re

from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon
from flexpy.Text import Text


# project_dir = "/home/wesley/Horokoi/FLEx/"
project_dir = "/home/kuhron/horokoi/FLEx/"  # WSL on field laptop C
project_name = "Horokoi"
fp = os.path.join(project_dir, project_name, f"{project_name}.fwdata")
corpus = Corpus(fp=fp, include_punctuation=False)

pattern = r"(khu|mai|mu|p[uia]|mana|ne|p[iu]n?[ae])[^\w]*?kha[iw]"
output_fp = "HorokoiCompoundTenseExamplesRaw.tsv"
corpus.write_paragraphs_matching_regex(pattern, output_fp)
