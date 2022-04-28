import re

from flexpy.FlexPyUtil import get_single_child
from flexpy.LexEntry import LexEntry
from flexpy.TagDict import TagDict



class Lexicon:
    """Contains the information in the FLEx database's lexicon.

    :param lex_entry_els:
    :type lex_entry_els: list(xml.etree.ElementTree.Element)
    :param tag_dict:
    :type tag_dict: :class:`flexpy.TagDict.TagDict`
    """
    def __init__(self, lex_entry_els, tag_dict):
        self.lex_entry_els = lex_entry_els
        self.tag_dict = tag_dict
        self.lex_entries = self.create_lex_entries()

    @staticmethod
    def from_project_dir_and_name(project_dir, project_name):
        tag_dict = TagDict.from_project_dir_and_name(project_dir, project_name)
        return Lexicon.from_tag_dict(tag_dict)

    @staticmethod
    def from_tag_dict(tag_dict):
        lex_entries = tag_dict["RtLexEntry"]
        return Lexicon(lex_entries, tag_dict)

    def create_lex_entries(self):
        res = []
        for guid, rts_with_guid in self.lex_entry_els.items():
            for rt in rts_with_guid:
                lex_entry = LexEntry(rt, self.tag_dict)
                res.append(lex_entry)
        return res

    def search_glosses(self, regex):
        """Searches the lexicon's glosses for a regex
        """
        results = []

        for lex_entry in self.lex_entries:
            for gloss in lex_entry.glosses:
                matches = re.search(regex, gloss)
                if matches is not None:
                    results.append(lex_entry)
                    break  # don't double-add it if multiple senses match
        return results

