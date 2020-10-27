import re

from flexpy.FlexPyUtil import get_single_child
from flexpy.LexEntry import LexEntry



class Lexicon:
    def __init__(self, lex_entry_els, rt_dict):
        self.lex_entry_els = lex_entry_els
        self.rt_dict = rt_dict
        self.lex_entries = self.create_lex_entries()

    def create_lex_entries(self):
        res = []
        for guid, rt in self.lex_entry_els.items():
            lex_entry = LexEntry(rt, self.rt_dict)
            res.append(lex_entry)
        return res

    def search_glosses(self, regex):
        results = []

        for lex_entry in self.lex_entries:
            for gloss in lex_entry.glosses:
                matches = re.search(regex, gloss)
                if matches is not None:
                    results.append(lex_entry)
                    break  # don't double-add it if multiple senses match
        return results

