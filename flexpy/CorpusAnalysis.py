import math
import numpy as np

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


# this function is copied directly from https://github.com/kristopherkyle/corpus_toolkit/blob/b5f0eba13dee60a0b56a25c5f3f900fe7c8c8cb4/build/lib/corpus_toolkit/corpus_tools.py
# and then modified for the sake of me being able to turn in the assignment sooner
def collocator_separating_target_and_collocate_terms(
        corpus_in_target_terms,
        corpus_in_collocate_terms,
        target, left=4, right=4, stat="MI", cutoff=5, ignore=None,
        ): 
    # returns a dictionary of collocation values
    # "in target terms" means the items in the corpus are converted
    # - in such a way that certain targets are treated the same
    # - e.g. you want to see which words correlate most with any verb
    # - so you modify the corpus to replace all verbs with "V", and that is 
    # - the corpus_in_target_terms argument
    # "in collocate terms" means the items in the corpus are converted
    # - in such a way that the collocates may be grouped similarly
    # - so in the "what collocates with any verb" analysis
    # - you may want all target verbs to be treated the same,
    # - but not all collocate verbs; you want the collocate verbs to retain their form
    # the target param is, of course, in target terms

    if ignore is None:  # no mutable default args
        ignore = []

    def corpus_iterator(corpus):
        for x in corpus:
            yield x

    # corpus, freq_corp = itertools.tee(corpus) #this makes two versions of the iterator so that it can be processed twice
    corp_freq_target_terms = ct.frequency(corpus_iterator(corpus_in_target_terms)) #use the frequency function to create frequency list
    corp_freq_colloc_terms = ct.frequency(corpus_iterator(corpus_in_collocate_terms))

    # these are number of TOKENS, not number of types (the values in the dict are counts of each type)
    nwords_target_terms = sum(corp_freq_target_terms.values()) #get corpus size for statistical calculations
    nwords_colloc_terms = sum(corp_freq_colloc_terms.values())
    assert nwords_target_terms == nwords_colloc_terms
    nwords = nwords_target_terms

    collocate_freq = {} #empty dictionary for storing collocation frequencies
    r_freq = {} #for hits to the right
    l_freq = {}  #for hits to the left
    stat_dict = {} #for storing the values for whichever stat was used
    
    def freq(l,d): #this takes a list (l) and a dictionary (d) as arguments
        for x in l: #for x in list
            if x in ignore:
                continue
            if x not in d: #if x not in dictionary
                d[x] = 1 #create new entry
            else: #else: add one to entry
                d[x] += 1
    
    #begin collocation frequency analysis
    for text_in_target_terms, text_in_colloc_terms in zip(corpus_in_target_terms, corpus_in_collocate_terms):
        assert len(text_in_target_terms) == len(text_in_colloc_terms)
        if target not in text_in_target_terms: #if target not in the text, don't search it for other words
            continue
        else:
            last_index = len(text_in_target_terms) -1 #get last index number
            for i in range(len(text_in_target_terms)):
                word_in_target_terms = text_in_target_terms[i]
                word_in_colloc_terms = text_in_colloc_terms[i]
                if word_in_target_terms == target:
                    start = i-left #beginning of left span
                    end = i + right + 1 #end of right span. Note, we have to add 1 because of the way that slices work in python
                    if start < 0: #if the left span goes beyond the text
                        start = 0 #start at the first word
                    #words to the right
                    lspan_list = text_in_colloc_terms[start:i] #for counting words on right
                    freq(lspan_list,l_freq) #update l_freq dictionary
                    freq(lspan_list,collocate_freq) #update collocate_freq dictionary
                    
                    rspan_list = text_in_colloc_terms[i+1:end] #for counting words on left. Note, have to add +1 to ignore node word
                    freq(rspan_list,r_freq) #update r_freq dictionary
                    freq(rspan_list,collocate_freq) #update collocate_freq dictionary
    
    #begin collocation stat calculation

    for x in collocate_freq:
        observed = collocate_freq[x]
        if observed < cutoff: #if the collocate frequency doesn't meet the cutoff, ignore it
            continue
        else:
            # TODO: this way of comparing frequencies among different form groupings might not be statistically sound
            expected = (corp_freq_target_terms[target] * corp_freq_colloc_terms[x])/nwords #expected = (frequency of target word (in entire corpus) * frequency of collocate (in entire corpus)) / number of words in corpus

            if stat == "MI":
                mi_score = math.log2(observed/expected)
                stat_dict[x] = mi_score
            elif stat == "T":
                try:
                    t_score = math.log2((observed - expected)/math.sqrt(expected))
                except ValueError:
                    # domain of log is strictly positive
                    better_error_str = "domain error with observed = {}, expected = {}, diff = {}; returning t-score of NaN".format(observed, expected, observed-expected)
                    print(better_error_str)
                    t_score = np.nan
                stat_dict[x] = t_score
            elif stat == "freq":
                stat_dict[x] = collocate_freq[x]
            elif stat == "right":
                if x in r_freq:
                    stat_dict[x] = r_freq[x] 
            elif stat == "left":
                if x in l_freq:
                    stat_dict[x] = l_freq[x]
                
    return(stat_dict)


