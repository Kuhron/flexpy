# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.FlexPyUtil import get_top_n_dict_items


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

