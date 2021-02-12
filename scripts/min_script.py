# Kris's library
from corpus_toolkit import corpus_tools as ct

# FlexPy-specific classes
from flexpy.Corpus import Corpus
from flexpy.TagDict import TagDict
from flexpy.Text import Text
from flexpy.FlexPyUtil import get_top_n_dict_items

import flexpy.CorpusAnalysis as corp



def perform_min_analysis(texts):
    # pass a list of strs, one for each text
    get_new_tokenized = lambda: ct.tokenize(texts, lemma=False)  # necessary because tokenize returns a generator, and then calling frequency or collocator or whatever will run it to StopIteration, so you have to get a new one each time
    freq = ct.frequency(get_new_tokenized())
    # ct.head(freq, hits=10)

    words_of_interest = ["เอา"]
    # get all ngrams
    n = 2
    ngrams = ct.tokenize(texts, lemma=False, ngram=n)
    ngram_freq = ct.frequency(ngrams)

    # subset of these ngrams where word of interest is present somewhere
    keys_containing_words_of_interest = [k for k in ngram_freq.keys() if any(w in k for w in words_of_interest)]
    freqs_of_interest_anywhere = {k: ngram_freq[k] for k in keys_containing_words_of_interest}
    print("\n---- ngrams containing words of interest anywhere ----")
    ct.head(freqs_of_interest_anywhere, hits=10)

    # subset of these ngrams where word of interest is at the beginning
    keys_beginning_with_words_of_interest = [k for k in ngram_freq.keys() if any(k[:len(w)] == w for w in words_of_interest)]
    freqs_of_interest_beginning = {k: ngram_freq[k] for k in keys_beginning_with_words_of_interest}
    print("\n---- ngrams containing words of interest at beginning ----")
    ct.head(freqs_of_interest_beginning, hits=10)

    # subset of these ngrams where word of interest is at the end
    keys_ending_with_words_of_interest = [k for k in ngram_freq.keys() if any(k[-len(w):] == w for w in words_of_interest)]
    freqs_of_interest_ending = {k: ngram_freq[k] for k in keys_ending_with_words_of_interest}
    print("\n---- ngrams containing words of interest at end ----")
    ct.head(freqs_of_interest_ending, hits=10)

    # show collocations of most frequent words or words of interest
    # n_most_frequent_words = 5
    # collocation_words_tups = get_top_n_dict_items(freq, n_most_frequent_words)
    metrics = ["MI", "T", "freq", "right", "left"]
    # for word, _ in collocation_words_tups:
    for word in words_of_interest:
        for metric in metrics:
            collocates = ct.collocator(get_new_tokenized(), word, stat=metric)
            print("----\nCollocations for {} using stat={}:".format(word, metric))
            ct.head(collocates, hits=10)



if __name__ == "__main__":
    project_name = "Isan"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name, include_punctuation=False)
    contents = corpus.get_contents()

    print("corpus size: {}".format(corp.get_corpus_size_words(contents)))
    perform_min_analysis(contents)
