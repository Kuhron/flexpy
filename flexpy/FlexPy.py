from xml.etree import ElementTree as ET
import random

# Kris's library
from corpus_toolkit import corpus_tools as ct

# FlexPy-specific classes
from flexpy.FlexPyUtil import get_single_child
from flexpy.RtDict import RtDict
from flexpy.Text import Text


def get_elements_by_owner_guid(rt_dict, owner_guid):
    return rt_dict.get_by_owner_guid(owner_guid)


def get_texts(rt_dict):
    text_elements = rt_dict["Text"]
    texts = []
    for guid, rt in text_elements.items():
        text = Text(guid, rt, rt_dict)
        texts.append(text)
    print("there are {} texts with contents".format(sum(x.has_contents() for x in texts)))
    return texts


def get_frequencies_naive(strs):
    assert type(strs) is list
    d = {}
    chars_to_delete = ".,/?!;\'\""
    for s in strs:
        for c in chars_to_delete:
            s = s.replace(c, "")
        words = s.lower().strip().split()
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
    return d


def report_frequencies_naive(strs):
    d = get_frequencies_naive(strs)
    tups = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    top_n = 50
    total_words = sum(d.values())
    print("---- report of top {} most frequent words (naive) out of {} words total ----".format(top_n, total_words))
    for tup in tups[:top_n]:
        print("Word {0} occurs {1} times".format(*tup))


def get_top_n_dict_items(dct, n):
    return sorted(dct.items(), key=lambda kv: kv[1], reverse=True)[:n]


def get_corpus_size_words(texts):
    tokenized = ct.tokenize(texts, lemma=False)
    return sum(len(x) for x in tokenized)


def perform_kris_analysis(texts):
    # pass a list of strs, one for each text
    get_new_tokenized = lambda: ct.tokenize(texts, lemma=False)  # necessary because tokenize returns a generator, and then calling frequency or collocator or whatever will run it to StopIteration, so you have to get a new one each time
    freq = ct.frequency(get_new_tokenized())
    ct.head(freq, hits=10)

    collocation_words_tups = get_top_n_dict_items(freq, 5)
    for word, _ in collocation_words_tups:
        collocates = ct.collocator(get_new_tokenized(), word, stat="MI")
        print("----\nCollocations for {}:".format(word))
        ct.head(collocates, hits=10)

    # could do some keyness between different pairs of texts

    for ngram_n in [2, 3, 4]:
        tokenized_ngram = ct.tokenize(texts, lemma=False, ngram=ngram_n)
        ngram_freq = ct.frequency(tokenized_ngram)
        print("----\n{}-grams:".format(ngram_n))
        ct.head(ngram_freq, hits=10)



if __name__ == "__main__":
    config = {}
    with open("FlexPyConfig.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue
            k, v = line.split("=")
            config[k.strip()] = v.strip()

    project_name = config["project_name"]
    project_dir = config["project_dir"]
    flex_dir = project_dir + "{}/".format(project_name)
    fp = flex_dir + "{}.fwdata".format(project_name)
    print("processing project {} at {}".format(project_name, fp))

    # in vim, type gg=G in normal mode (no colon) to indent xml file
    # this works because I added the following in ~/.vimrc
    # :set equalprg=xmllint\ --format\ -
    # and can type ':set nowrap' (no quotes) to stop wrapping the long lines of semantic domain descriptions
    # easier to see the .fwdata structure this way
 
    # tree = ET.parse(fp)
    # root = tree.getroot()
    rt_dict = RtDict.from_fwdata_file(fp)

    texts = get_texts(rt_dict)
    contents_lst = []
    for text in texts:
        # print("----")
        # print(text)
        contents = text.get_contents()
        # print(contents)
        contents_lst += contents
        # print("----\n")

    print("corpus size: {}".format(get_corpus_size_words(contents_lst)))
    # report_frequencies_naive(contents_lst)
    perform_kris_analysis(contents_lst)
