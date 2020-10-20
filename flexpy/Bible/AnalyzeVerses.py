import itertools
import os
import random
import string
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Scraping import (
    get_book_info, get_verse_dict
)


# print the bible verses, pipe it to file when it's working as you want

def walk_verse_strings(lang_iso_code, print_interleaved, print_parseable, return_full_list, books_to_restrict_to=None):
    parseable_fp = "texts/{0}/{0}-VersesParseable.txt".format(lang_iso_code)
    if os.path.exists(parseable_fp):
        print("using parseable verse file")
        # read this instead of the html
        # allows me to put in propositional act functions in the text itself
        lang_verses_all = []
        with open(parseable_fp) as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue
            verse = line.split(" ")
            # if any(":" in x for x in verse):
            #     print("got delim in verse: {}".format(verse))
            lang_verses_all.append(verse)
    else:
        print("parseable verse file not found, using html instead")
        # just put all bible verses in order first, for both languages
        print("getting verse strings")
        book_info = get_book_info()
        if books_to_restrict_to is not None:
            book_info = [(book_abbrev, n_chaps) for book_abbrev, n_chaps in book_info if book_abbrev in books_to_restrict_to]
        
        lang_bible_dict = {}
        english_bible_dict = {}
        
        for book_abbrev, n_chaps in book_info:
            lang_bible_dict[book_abbrev] = {i: {} for i in range(1, n_chaps+1)}
            english_bible_dict[book_abbrev] = {i: {} for i in range(1, n_chaps+1)}
            for chap_num in range(1, n_chaps+1):
                lang_verse_dict = get_verse_dict(lang_iso_code, book_abbrev, chap_num)
                english_verse_dict = get_verse_dict("eng", book_abbrev, chap_num)
                lang_bible_dict[book_abbrev][chap_num] = lang_verse_dict
                english_bible_dict[book_abbrev][chap_num] = english_verse_dict
        
        lang_verses_all = []
        for abbrev, n_chaps in book_info:
            for c in range(1, n_chaps+1):
                lang_chap = lang_bible_dict[abbrev][c]
                english_chap = english_bible_dict[abbrev][c]
                max_v = max(set(lang_chap.keys()) | set(english_chap.keys()))
                for v in range(1, max_v+1):
                    lang_verse_str = lang_chap.get(v, "-")
                    english_verse_str = english_chap.get(v, "-")

                    if print_interleaved:
                        lang_str = "{} {}:{} {} = {}".format(abbrev, c, v, lang_iso_code, lang_verse_str)
                        english_str = "{} {}:{} eng = {}".format(abbrev, c, v, english_verse_str)
                        print(lang_str)
                        print(english_str)
                        print()

                    if return_full_list:
                        if lang_verse_str == "-":
                            continue  # don't do any of the collocational stuff
                        delete_chars = [","]
                        delete_chars += list("0123456789")
                        turn_into_period_chars = [":", ";", "\"", "“", "”", "'", "‘", "’", "!", "?", "[", "]", "(", ")"]
                        add_spaces_around_chars = ["."]
                        okay_chars = string.ascii_lowercase + " .-ŋñ"
                        cleaned_verse = lang_verse_str.lower()
                        for char in delete_chars:
                            cleaned_verse = cleaned_verse.replace(char, "")
                        for char in turn_into_period_chars:
                            cleaned_verse = cleaned_verse.replace(char, ".")
                        for char in add_spaces_around_chars:
                            cleaned_verse = cleaned_verse.replace(char, " "+char+" ")
                        cleaned_verse_no_alpha = set(cleaned_verse) - set(okay_chars)
                        if len(cleaned_verse_no_alpha) > 0:
                            print("extra chars in {} {}:{}:\n{}".format(abbrev, c, v, cleaned_verse_no_alpha))
                            input("press enter to continue")
                        cleaned_verse_lst = cleaned_verse.split()
                        cleaned_verse_lst = [x for x in cleaned_verse_lst if x != ""]
                        lang_verses_all.append(cleaned_verse_lst)
                        if print_parseable:
                            print("# {abbrev} {c}:{v}".format(**locals()))
                            print("# {lang_verse_str}".format(**locals()))
                            print(" ".join(cleaned_verse_lst))
                            print("# {english_verse_str}".format(**locals()))
                            print()

    if return_full_list:
        assert type(lang_verses_all) is list and all(type(x) is list for x in lang_verses_all)
        raw_full_lst = []
        for sub_lst in lang_verses_all:
            raw_full_lst += sub_lst
        full_lst = ["."]  # start off with sentence boundary so we know what occurs around sentence boundary
        for w in raw_full_lst:
            if full_lst[-1] == "." and w == ".":
                # remove duplicate period strings
                continue
            full_lst.append(w)
        if full_lst[-1] != ".":
            full_lst.append(".")

        print("done getting full list of verse strings")
        return full_lst  # flat structure


def get_collocation_matrix(full_lst, 
                           specified_words, specified_environments,
                           # n_most_common_words=None, n_most_common_environments=None,
                           environment_expansions=None, use_propositional_act_functions=True):
    if environment_expansions is not None:
        for k, lst in environment_expansions.items():
            assert k not in lst, "recursion in environment expansions not allowed right now due to diminishing returns from writing complicated code"
            assert k != "_", "can't expand blanks"
            for x in lst:
                assert x != "_", "can't expand to blank, k {}, x {}".format(k, x)
                assert type(x) is str, "can't expand to non-str, k {}, x {}".format(k, x)
                assert " " not in x, "can't expand to str with space, k {}, x {}".format(k, x)

    specified_environments = [tuple(env.split()) for env in specified_environments]
    # all_words = set(full_lst)
    # all_environments = set()
    # collocations = {}
    # word_occurrences = {}
    # environment_occurrences = {}
    # for i, w in enumerate(full_lst):
        # if i % 10000 == 0:
        #     print("progress: i = {}/{}\r".format(i, len(full_lst)))
        # if specified_words is not None and w not in specified_words:
        #     continue

        # if w in word_occurrences:
        #     word_occurrences[w] += 1
        # else:
        #     word_occurrences[w] = 1
        # all_words.add(w)

        # environments = []
        # if i != 0 and i != len(full_lst) - 1:
        #     mid_environment = " ".join([full_lst[i-1], "_", full_lst[i+1]])
        #     environments.append(mid_environment)
        # if i != 0:
        #     before_environment = " ".join([full_lst[i-1], "_"])
        #     environments.append(before_environment)
        # if i != len(full_lst) - 1:
        #     after_environment = " ".join(["_", full_lst[i+1]])
        #     environments.append(after_environment)
        
        # if w in collocations:
        #     d = collocations[w]
        # else:
        #     d = {}

        # for env in environments:
        #     if specified_environments is not None and env not in specified_environments:
        #         continue

        #     if env in environment_occurrences:
        #         environment_occurrences[env] += 1
        #     else:
        #         environment_occurrences[env] = 1
        #     all_environments.add(env)

        #     if env in d:
        #         d[env] += 1
        #     else:
        #         d[env] = 1

        # collocations[w] = d
        # print("\ni = {}\nword = {}\ncollocations = {}".format(i, w, d))

    # add zeros to collocation counts that were not found; makes huge sparse matrix
    # for w in all_words:
    #     for env in all_environments:
    #         if env not in collocations[w]:
    #             collocations[w][env] = 0

    # if n_most_common_words is not None:
    #     words_most_common = sorted(word_occurrences.items(), key=lambda kv: kv[1], reverse=True)
    #     word_keys = [k for k,v in words_most_common[:n_most_common_words]]
    # elif specified_words is not None:
    #     word_keys = specified_words
    # else:
    #     word_keys = all_words

    # if n_most_common_environments is not None:
    #     envs_most_common = sorted(environment_occurrences.items(), key=lambda kv: kv[1], reverse=True)
    #     environment_keys = [k for k,v in envs_most_common[:n_most_common_environments]]
    # elif specified_environments is not None:
    #     environment_keys = specified_environments
    # else:
    #     environment_keys = all_environments

    # for w, n_occ in sorted(occurrences.items(), key=lambda kv: kv[1], reverse=True):
    #     # most occurring words first
    #     # print("\nword {}\n{} occurrences\ncollocations:".format(w, n_occ))
    #     for env, n_coll in sorted(collocations[w].items(), key=lambda kv: kv[1], reverse=True)[:n_envs_to_show]:
    #         print(env, n_coll)
    #     input("press enter to continue")

    # new_collocations = {}
    # for w in word_keys:
    #     d = {}
    #     for env in environment_keys:
    #         d[env] = collocations[w].get(env, 0)
    #     new_collocations[w] = d
    # collocations = new_collocations

    # ^^^ OLD WAY ^^^

    propositional_act_functions = ["R", "M", "P", "?"]  # reference, modification, predication
    env_strs = [" ".join(env) for env in specified_environments]
    env_paf_tups = [(env_str, paf) for env_str in env_strs for paf in propositional_act_functions]

    # environments_expanded = expand_environments(specified_environments, environment_expansions)
    if use_propositional_act_functions:
        collocations = {w: {tup: 0 for tup in env_paf_tups} for w in specified_words}
    else:
        collocations = {w: {env_str: 0 for env_str in env_strs} for w in specified_words}
    # assign a word to macro-env (unexpanded) if it is found in one of the more specific ones from the expansion list

    # for macro_env, micro_env_lst in environments_expanded.items():
    # for env_i, macro_env in enumerate(sorted(environments_expanded.keys())):
    for env_i, env in enumerate(specified_environments):
        print("env = {} (#{}/{})".format(env, env_i+1, len(specified_environments)))
        env_str = " ".join(env)
        # micro_env_lst = environments_expanded[macro_env]
        # for env in micro_env_lst:
            # iterate through the whole list of words, collect matches
        assert env.count("_") == 1
        blank_position = env.index("_")
        length_deviation = len(env) - 1  # if len(env) == 1, then just get every slice, starting at every index; lop one off for every extra element of env
        for i in range(len(full_lst) - length_deviation):
            test_env = full_lst[i : i+len(env)]
            w = test_env[blank_position]
            # print("w = {}".format(w))
            if use_propositional_act_functions and ":" in w:
                # propositional act function has been specified by user
                # print("got word with delim for paf: {}".format(w))
                # input("check")
                w, paf = w.split(":")
                assert paf in propositional_act_functions, "invalid PAF {}\nw = {}, env = {}".format(paf, w, env)
            else:
                # don't know paf
                paf = "?"
            tup = (env_str, paf)

            if w not in specified_words:
                # don't waste any more time
                continue
            pattern_env = env
            if matches_environment(test_env, pattern_env, environment_expansions):
                if use_propositional_act_functions:
                    collocations[w][tup] += 1
                else:
                    collocations[w][env_str] += 1

    word_keys = specified_words
    env_keys = env_paf_tups if use_propositional_act_functions else env_strs
    def env_sort_function(env):
        if type(env) is str:
            return env
        env_str, paf = env
        first_sort_val = "RMP?".index(paf)
        second_sort_val = env_str
        return (first_sort_val, second_sort_val)
    env_keys = sorted(env_keys, key=env_sort_function)

    df = pd.DataFrame.from_dict(collocations, orient="index")
    df = df.reindex(index=word_keys, columns=env_keys)  # re-sort rows and columns because dict put them out of order
    return df


def expand_environments(envs, expansions):
    raise Exception("do not use")
    print("expanding envs:\nenvs = {}\nexpansions = {}\n".format(envs, expansions))
    # input("check for correctness")
    res = {}
    for env in envs:
        expansion_of_this_env = []
        possibilities_per_element = []
        for element in env:
            if element in expansions:
                possibilities = expansions[element]
            else:
                possibilities = [element]  # only one possibility, the item itself
            possibilities_per_element.append(possibilities)
        cartesian_product = itertools.product(*possibilities_per_element)  # list of tuples, each of which is a point in the space
        for point in cartesian_product:
            expansion_of_this_env.append(tuple(point))
        res[env] = expansion_of_this_env

    # do not recursively call

    # res = sorted(set(res))

    print("finished expanding envs")
    return res


def matches_environment(test_env, pattern_env, expansions):
    # print("\ntesting if envs match:\ntest    = {}\npattern = {}".format(test_env, pattern_env))
    if len(test_env) != len(pattern_env):
        # print("len mismatch --> False\n")
        return False
    for a, b in zip(test_env, pattern_env):
        if b == "_":  # the blank where something can go, don't check equality of this in the test env
            # print("skipping blank, a = {}, b = {}".format(a, b))
            continue
        if not elements_match(a, b, expansions):
            # print("unequal --> False; a = {}, b = {}\n".format(a, b))
            return False
    # print("match! --> True\n")
    return True


def elements_match(test_element, pattern_element, expansions):
    if pattern_element == "_":
        return True
    elif test_element == pattern_element:
        return True
    elif pattern_element in expansions:
        possibilities = expansions[pattern_element]
        return any(elements_match(test_element, possibility, expansions) for possibility in possibilities)
    else:
        return False


def convert_matrix_to_01(m, condition_function):
    if type(m) is list:
        return [[int(condition_function(x)) for x in row] for row in m]
    elif type(m) is pd.DataFrame:
        return m.apply(condition_function).astype(int)
    else:
        raise TypeError


def print_interleaved(lang_iso_code):
    walk_verse_strings(lang_iso_code, print_interleaved=True, return_full_list=False)
    # should return None


def get_full_list(lang_iso_code, **kwargs):
    return walk_verse_strings(lang_iso_code, print_interleaved=False, print_parseable=False, return_full_list=True, **kwargs)


def get_kalam_dictionary_items():
    input_fp = "texts/kmh/KalamDictionary.txt"
    with open(input_fp) as f:
        lines = f.readlines()
    res = []  # just make list of tuples
    for line in lines:
        if line[0] == "#":
            continue
        line = line.strip()
        bible_ortho, pawley_ortho, gloss, concept_type = line.split(" = ")
        tup = (bible_ortho, pawley_ortho, gloss, concept_type)
        res.append(tup)
    return res


def get_distance_matrix_discrete_metric(df):
    res = pd.DataFrame(index=df.index, columns=df.index)
    for i, row_i in df.iterrows():
        for j, row_j in df.iterrows():
            if j < i:
                continue
            mask = (row_i != row_j).astype(int)
            d = mask.sum()
            res.loc[i, j] = res.loc[j, i] = d
    return res


def plot_occurrence_matrix(m, title):
    words = m.index.values
    envs = m.columns.values
    plt.imshow(np.array(m))
    plt.xticks(range(len(envs)), envs, rotation=90)
    plt.yticks(range(len(words)), words)
    plt.title(title)
    plt.colorbar()
    plt.show()


def plot_distance_matrix(distance_matrix, title):
    words = distance_matrix.index.values
    assert (words == distance_matrix.columns.values).all(), "distance matrix does not have same array of words for rows and columns\nrows: {}\ncols: {}".format(words, distance_matrix.columns.values)
    
    plt.imshow(distance_matrix)
    plt.xticks(range(len(words)), words, rotation=90)
    plt.yticks(range(len(words)), words)
    plt.title(title)
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    # print_interleaved("dnw")
    # walk_verse_strings("kmh", print_interleaved=False, print_parseable=True, return_full_list=True)
    # sys.exit()

    # books_to_restrict_to = ["MAT", "REV"]  # testing
    books_to_restrict_to = None  # everything
    kalam_verses = get_full_list("kmh", books_to_restrict_to=books_to_restrict_to)
    kalam_dictionary_items = get_kalam_dictionary_items()

    # prototype_nouns = [
    #     "bi", "biyn", "biynimb", "korip",
    #     "gor", "jiysis", "krays",
    # ]
    # prototype_medial_verbs = [
    #     "giy", "geyak", "mindiy", "mindip",
    #     # "amnak", "amiy", "amninik", "amniyak", 
    #     # "ayak", "aypay", 
    #     # "aŋgak", "aŋgyak", 
    # ]
    # prototype_final_verbs = [
    #     "gak", "giyak", "gisap", "gispiyn", "mindpiyn",
    # ]
    # prototype_verb_adjuncts = [
    #     "timb", "di", "ap", "am", "mind",
    # ]  # take these from Pawley's 1966 grammar
    # prototype_particles = [
    #     "ma",
    # ]
    # prototype_pronouns = [
    #     "yand", "yip", "nand", "nip", "nuk", "nup", "chin", "chinup", "nimb", "nimbik", "kiy", "kiyk",
    # ]

    # specified_words = prototype_nouns + prototype_medial_verbs + prototype_final_verbs + prototype_verb_adjuncts + prototype_particles + prototype_pronouns

    object_concepts = [bible_ortho for bible_ortho, pawley_ortho, gloss, concept_type in kalam_dictionary_items if concept_type == "object"]
    property_concepts = [bible_ortho for bible_ortho, pawley_ortho, gloss, concept_type in kalam_dictionary_items if concept_type == "property"]
    action_concepts = [bible_ortho for bible_ortho, pawley_ortho, gloss, concept_type in kalam_dictionary_items if concept_type == "action"]

    # specified_words = object_concepts + property_concepts + action_concepts
    # specified_words = random.sample(specified_words, 10)  # testing purposes
    # specified_words = ["yiwan", "yiwur", "pumb", "sikoy", "mosimb", "kanj"]
    specified_words = ["jiysis", "siypsiyp", "tomb", "mosimb", "yiwan", "tikak", "gayak"]

    specified_environments = [
        # "ma _",
        # "_ mind-",
        # "O _ mind-",
        # "_ kun/ak",
        # "O _", "_ O",
        # "tap _", "tap _ A",
        # "_ sek",
        "_ O",
        "_ sek",
        "O _",
        "tap _",
        "_ mind-",
        "_ (ak) mind-",
    ]

    environment_expansions = {
        "O": object_concepts,
        "P": property_concepts,
        "A": action_concepts,
        "mind-": ["mindip", "mindakniŋ", "mindiy", "mindeniŋgambay", "mindenimimb", "mindek", "mindyiŋgipay", "mindeniŋgamb", "mindeyak",],
        # "mind-": ["mindip", "mindiy"],  # testing purposes
        "kun/ak": ["kun", "ak"],
    }

    matrix = get_collocation_matrix(
        kalam_verses,
        specified_words=specified_words,
        # n_most_common_words=250,
        specified_environments=specified_environments,
        # n_most_common_environments=250,
        environment_expansions=environment_expansions,
        use_propositional_act_functions=True
    )
    # plot_occurrence_matrix(matrix, title="occurrences")

    # log_matrix = matrix.apply(np.log).replace(-np.inf, -1).fillna(-1)
    # plot_occurrence_matrix(log_matrix, title="log occurrences (-1 = not found)")

    matrix_01 = convert_matrix_to_01(matrix, lambda x: x > 0)
    plot_occurrence_matrix(matrix_01, title="occurrences boolean")
    # word_distance_matrix = get_distance_matrix_discrete_metric(matrix_01)
    # plot_distance_matrix(word_distance_matrix, "distances between words")
    # env_distance_matrix = get_distance_matrix_discrete_metric(matrix_01.transpose())
    # plot_distance_matrix(env_distance_matrix, "distances between environments")
