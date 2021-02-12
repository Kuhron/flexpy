import re
import pandas as pd

from flexpy.Corpus import Corpus
from flexpy.Text import Text
from flexpy.WordForm import WordForm, WordFormMorpheme



if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name, include_punctuation=False)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    # wordform_contents = corpus.get_wordform_contents(
    #     texts_separated=True,
    #     paragraphs_separated=False,
    #     texts_to_omit=texts_to_omit,
    # )
    contents = corpus.get_tokenized_contents(texts_to_omit=texts_to_omit)
    report_individual_matches = False  # for printing each token's line

    # token_regex = r"(^|\b)(?P<token>[pbtdkgqj][aeiou])\s?[^aoeuimnñŋlr]"  # certain word-initial stop-vowel combos
    onsets_segs = ["p", "t", "k", "b", "d", "g", "q", "j"]
    vowels_segs = ["a", "e", "i", "o", "u"]
    onsets = ["[{}]".format("".join(onsets_segs))]  # hack to get the regex to think of it as a single character class, and only iterate for loop for one onset
    # onsets = "d"
    all_counts = {}
    for onset in onsets:
        # token_regex = r"(^|\b)(?P<token>" + onset + "[aeiou]\s?[tds])"
        token_regex = r"(^|\b)(?P<token>" + onset + "[{}])".format("".join(vowels_segs))
        # find all matches of this regex
        counts_this_onset = {}
        for line_lst in contents:
            assert type(line_lst) is list, line_lst
            assert all(type(x) is str for x in line_lst), line_lst
            line_str = " ".join(line_lst)
            # https://stackoverflow.com/questions/11103856/re-findall-which-returns-a-dict-of-named-capturing-groups
            regex_matches = re.finditer(token_regex, line_str)
            for match in regex_matches:
                token = match.groupdict()["token"]
                token = token.replace(" ", "")
                if report_individual_matches:
                    print("match found: {} in line: {}".format(token, line_str))
                if token not in counts_this_onset:
                    counts_this_onset[token] = 0
                counts_this_onset[token] += 1
                if token not in all_counts:
                    all_counts[token] = 0
                all_counts[token] += 1
        print("\n-- token counts in entire corpus")
        for token, count in sorted(counts_this_onset.items()):
            print("{} : {} tokens".format(token, count))
        # print("total tokens of #CV not before nasal/liquid/vowel: {}".format(sum(counts.values())))
    
    counts_by_c_then_v = {c: {v: 0 for v in vowels_segs} for c in onsets_segs}
    # initialize all to 0, even the ones that don't show up at all, so we can make nice table
    for token, count in all_counts.items():
        assert len(token) == 2, token
        c, v = token
        counts_by_c_then_v[c][v] += count
    df = pd.DataFrame(counts_by_c_then_v)
    print(df)