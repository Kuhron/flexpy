import re

from flexpy.Corpus import Corpus
from flexpy.Text import Text
from flexpy.WordForm import WordForm, WordFormMorpheme



if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    # wordform_contents = corpus.get_wordform_contents(
    #     texts_separated=True,
    #     paragraphs_separated=False,
    #     texts_to_omit=texts_to_omit,
    # )
    contents = corpus.get_tokenized_contents(texts_to_omit=texts_to_omit)

    # token_regex = r"(^|\b)(?P<token>[pbtdkgqj][aeiou])\s?[^aoeuimnñŋlr]"  # certain word-initial stop-vowel combos
    for onset in "ptkbdgqj":
        token_regex = r"(^|\b)(?P<token>" + onset + "[aeiou]\s?[tds])"
        # find all matches of this regex
        counts = {}
        for line_lst in contents:
            assert type(line_lst) is list, line_lst
            assert all(type(x) is str for x in line_lst), line_lst
            line_str = " ".join(line_lst)
            # https://stackoverflow.com/questions/11103856/re-findall-which-returns-a-dict-of-named-capturing-groups
            regex_matches = re.finditer(token_regex, line_str)
            for match in regex_matches:
                token = match.groupdict()["token"]
                token = token.replace(" ", "")
                # print("match found: {} in line: {}".format(token, line_str))
                if token not in counts:
                    counts[token] = 0
                counts[token] += 1
        print("\n-- token counts in entire corpus")
        for token, count in sorted(counts.items()):
            print("{} : {} tokens".format(token, count))
        # print("total tokens of #CV not before nasal/liquid/vowel: {}".format(sum(counts.values())))
