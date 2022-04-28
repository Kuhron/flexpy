# implementation of methods from Hammarström's 2019 presentation
# "Prospects for a (Semi-)Automated Papuan Comparative Linguistics and Reconstruction"

import os
import random
from flexpy.Corpus import Corpus
from flexpy.WordDistance import levenshtein, normalized_levenshtein


class LexiconSimple:
    def __init__(self, language_name, lexemes):
        self.language_name = language_name
        self.lexemes = lexemes
    
    def get_glosses_set(self):
        res = set()
        for lex in self.lexemes:
            res |= set(lex.glosses)
        return res


class LexemeSimple:
    def __init__(self, forms, poses, glosses, language_name):
        assert type(forms) is list, forms
        assert type(poses) is list, poses
        assert type(glosses) is list, glosses
        self.forms = forms
        self.poses = poses
        self.glosses = glosses
        self.language_name = language_name
    
    def __repr__(self):
        return "<{} word {} = {}>".format(self.language_name, self.forms, self.glosses)


def load_lexicon_from_tsv(fp, language_name):
    print("loading tsv for lexicon of {}".format(language_name))
    with open(fp) as f:
        lines = f.readlines()
    lexemes = []
    for line in lines:
        forms_csv, pos_csv, gloss_csv = line.split("\t")
        forms = forms_csv.split(",")
        poses = pos_csv.split(",")
        if gloss_csv[-1] == "\n":
            gloss_csv = gloss_csv[:-1]
            assert "\n" not in gloss_csv
        glosses = gloss_csv.split(",")
        lexeme = LexemeSimple(forms, poses, glosses, language_name)
        lexemes.append(lexeme)
    lexicon = LexiconSimple(language_name, lexemes)
    return lexicon


def write_lexicon_tsv(corpus, fp):
    lexicon = corpus.lexicon
    lexicons[ln] = lexicon
    lex_entries = lexicon.lex_entries
    s = ""
    for lex_entry in lex_entries:
        s += lex_entry.tsv_repr() + "\n"
    with open(fp, "w") as f:
        f.write(s)


def get_similarity_measure(word_set):
    sum_similarity = get_sum_similarity(word_set)
    return sum_similarity / len(word_set)


def get_sum_similarity(word_set):
    sum_similarity = 0
    for pair in itertools.combinations(word_set, 2):
        a, b = pair
        assert a != b  # itertools shouldn't give multiplicity in combos but I'm paranoid
        similarity = get_pairwise_similarity(pair)
        sum_similarity += similarity
    return sum_similarity


def get_pairwise_levenshtein(word_pair):
    a, b = word_pair
    assert type(a) is LexemeSimple, a
    assert type(b) is LexemeSimple, b
    min_dist = None
    for af in a.forms:
        for bf in b.forms:
            dist = normalized_levenshtein(af, bf)
            if min_dist is None or dist < min_dist:
                min_dist = dist
    return min_dist


def get_pairwise_similarity(word_pair, other_words):
    return get_significance_similarity(word_pair, other_words)


def get_significance_similarity(word_pair, other_words):
    # Hammarström: proportion of words z with different meaning such that d(x,y) <= d(x,z)
    # (i.e. the proportion of random chance words which are beaten by y as potential match)
    # TODO does this need to be symmetrical for x and y? as stated right now it is not
    x,y = word_pair
    dxy = get_pairwise_levenshtein(word_pair)
    n_z = len(other_words)
    xy_simil_count = 0
    for z in other_words:
        dxz = get_pairwise_levenshtein((x,z))
        if dxy <= dxz:
            xy_simil_count += 1
    return xy_simil_count / n_z


def find_random_pair_identical_glosses(lexicons):
    while True:
        lexicon1, lexicon2 = random.sample(list(lexicons.values()),2)
        glosses1 = lexicon1.get_glosses_set()
        glosses2 = lexicon2.get_glosses_set()
        overlap = glosses1 & glosses2
        if len(overlap) == 0:
            print("no glosses in common between {} and {}".format(lexicon1.language_name, lexicon2.language_name))
            continue
        chosen = random.choice(list(overlap))
        lexeme1 = random.choice([lex for lex in lexicon1.lexemes if chosen in lex.glosses])
        lexeme2 = random.choice([lex for lex in lexicon2.lexemes if chosen in lex.glosses])
        print("chose gloss {}, words {}: {} and {}: {}".format(chosen, lexicon1.language_name, 
            lexeme1.forms, lexicon2.language_name, lexeme2.forms)
        )
        other_words1 = [lex for lex in lexicon1.lexemes if chosen not in lex.glosses]
        other_words2 = [lex for lex in lexicon2.lexemes if chosen not in lex.glosses]
        return lexeme1, lexeme2, other_words1, other_words2


def test_show_similarity(lexicons):
    print("-- getting test pair of words to show similarity measure")
    lex1, lex2, ow1, ow2 = find_random_pair_identical_glosses(lexicons)
    simil12 = get_significance_similarity((lex1, lex2), ow2)
    simil21 = get_significance_similarity((lex2, lex1), ow1)
    print("significance similarity of word 1 among words in language 2 = {}".format(simil12))
    print("significance similarity of word 2 among words in language 1 = {}".format(simil21))
    print("-- done testing similarity\n")


def get_all_similarities(lexicon1, lexicon2, glosses=None):
    ln1 = lexicon1.language_name
    ln2 = lexicon2.language_name
    d = {ln1: {}, ln2: {}}
    if glosses is not None:
        lexemes1 = [lex for lex in lexicon1.lexemes if any(g in lex.glosses for g in glosses)]
        lexemes2 = [lex for lex in lexicon2.lexemes if any(g in lex.glosses for g in glosses)]
    else:
        lexemes1 = lexicon1.lexemes
        lexemes2 = lexicon2.lexemes
    for lex1_i, lex1 in enumerate(lexemes1):
        print("lex1 #{}/{}".format(lex1_i, len(lexemes1)))
        if lex1 not in d[ln1]:
            d[ln1][lex1] = {}
        for lex2_i, lex2 in enumerate(lexemes2):
            print("lex2 #{}/{}".format(lex2_i, len(lexemes2)))
            if lex2 not in d[ln2]:
                d[ln2][lex2] = {}
            other_words1 = [lex for lex in lexemes1 if lex is not lex1]
            other_words2 = [lex for lex in lexemes2 if lex is not lex2]
            simil12 = get_significance_similarity((lex1, lex2), other_words2)
            simil21 = get_significance_similarity((lex2, lex1), other_words1)
            d[ln1][lex1][lex2] = simil12
            d[ln2][lex2][lex1] = simil21
    return d



if __name__ == "__main__":
    language_names = [
        # wesley@lumen:~/.local/share/fieldworks/Projects$ ls | xargs -d "\t" echo | sed -e "s/^/\"/g" | sed -e "s/$/\",/g"
        # "Acoma",  # not Papuan!
        "Aisi Mabɨŋ",
        "Aisi Magɨ",
        "Bara",
        "Bere",
        "Bongu",
        # "dnw-flex",  # not Madang
        "Gants",
        # "Isan",  # not Papuan!
        "Kursav",
        "Manat",
        "Mand",
        "Sa",
        "Sirva",
        "Soq",
        # "test",
        "Yangulam",
    ]
    print("found {} languages".format(len(language_names)))
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    lexicons = {}
    wordlist_dir = "/home/wesley/flexpy/flexpy/language_data/MadangWordlists/"
    for ln in language_names:
        print("-- loading language {}".format(ln))
        filename = "{}.tsv".format(ln)
        fp = os.path.join(wordlist_dir, filename)
        if os.path.exists(fp):
            lexicon = load_lexicon_from_tsv(fp, ln)
            lexicons[ln] = lexicon
        else:
            print("creating tsv for lexicon of {}".format(ln))
            corpus = Corpus(project_dir, ln, include_punctuation=False)
            write_lexicon_tsv(corpus, fp)
            assert os.path.exists(fp)  # should be there now that we wrote it
            lexicon = load_lexicon_from_tsv(fp, ln)
            lexicons[ln] = lexicon

        print("{} has {} lexeme entries".format(ln, len(lexicon.lexemes)))

    test_show_similarity(lexicons)
    lexicon1, lexicon2 = random.sample(list(lexicons.values()),2)
    glosses = ["man", "woman", "canoe", "sun", "red", "cloth", "coconut", "salt", "water",
        "cassowary", "pandanus", "liver", "hot", "fish", "speak", "tooth", "louse",
    ]
    all_similarities = get_all_similarities(lexicon1, lexicon2, glosses)
    for ln in all_similarities:
        print("\n-- language {}".format(ln))
        for lex1 in all_similarities[ln]:
            print("word {}".format(lex1))
            most_similar = sorted(all_similarities[ln][lex1].items(), key=lambda kv:kv[1], reverse=True)
            for lex2, score in most_similar:
                print("{}\t\t{:.2f}".format(lex2, score))
            print()
        print()
    # print(all_similarities)