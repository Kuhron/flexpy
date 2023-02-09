import re

from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon
from flexpy.Text import Text


fp = "/home/wesley/Desktop/PUP.fwdata"
corpus = Corpus(fp, include_punctuation=False)

fpst = r"nd[ua]"
ds = r"nd(e|na|ne)"
lnk = r"e"
prs = r"s[a]|na"
hab = r"m(a|e|blu|u)"
fut = r"ŋsan|san|ŋgu|ŋsunu|ŋsnu|sunu"
bare = "\b"
sfx = "(" + "|".join([fpst, ds, lnk, prs, hab, fut, bare]) + ")"
# sfx = f"({fpst}|{prs})"  # debug

for stem in ["bu", "pei", "bara", "me", "ka", "wa"]:
    pattern = r"\b(ka|ba)?" + stem + sfx
    print(pattern)
    output_fp = f"SaLocativeExamples_{stem}_Raw.tsv"
    corpus.write_paragraphs_matching_regex(pattern, output_fp)
