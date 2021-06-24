# testing Kris's library
from corpus_toolkit import corpus_tools as ct
import KrisCorpusToolsDebugging as ct_debug
# documentation at https://github.com/kristopherkyle/corpus_toolkit

text1 = "cat cat dog cat elephant"
text2 = "the of and a to in is that it was"
text3 = "a a a a a aa a a a aa aaaaa"
texts = [text1, text2, text3]
tokenized = ct.tokenize(texts)
freq = ct.frequency(tokenized)
ct.head(freq, hits=5)
# frequency function iterates over "tokenized texts" first, then over ttokens in those texts, so input must be an iterable of iterables
# see source at https://github.com/kristopherkyle/corpus_toolkit/blob/b5f0eba13dee60a0b56a25c5f3f900fe7c8c8cb4/build/lib/corpus_toolkit/corpus_tools.py

# what if I include capitals and punctuation
print("----")
text4 = "Cat? Dog! A man, a plan, a canal, Panama! A dog, a panic in a pagoda. Most most most most most most most most most, most? Most! MOST... most?!?! most: Most most most most most most, (most) [most]."
texts.append(text4)
tokenized = ct.tokenize(texts)
freq = ct.frequency(tokenized)
ct.head(freq, hits=10)


print("----")
corpora_dir = "/home/wesley/Desktop/UOregon Work/CorpusLinguistics/corpora/"
text_files = ["dracula.txt", "wuthering_heights.txt"]
texts = []
for text_file in text_files:
    fp = corpora_dir + text_file
    with open(fp) as f:
        contents = f.read()
        texts.append(contents)
tokenized = ct.tokenize(texts)
freq = ct.frequency(tokenized)
ct.head(freq, hits=10)


# Collocations
print("----")
words_to_collocate = ["the"]
for word in words_to_collocate:
    tokenized = ct.tokenize(texts)  # WARNING! have to do this again because it returns a generator, so I was getting no collocations because it had already reached StopIteration from calling frequency() on it before
    collocates = ct.collocator(tokenized, word, stat="MI")
    # collocates = ct_debug.collocator(tokenized, word, stat="MI")
    # print("collocations for word {}:".format(word))
    # print("collocates =", collocates)
    ct.head(collocates, hits=10)


# Keyness
# see http://www.thegrammarlab.com/?p=193
# and https://en.wikipedia.org/wiki/Keyword_(linguistics)
print("----")
corp1 = texts[:1]
corp2 = texts[1:]
corp1_freq = ct.frequency(ct.tokenize(corp1))
corp2_freq = ct.frequency(ct.tokenize(corp2))
corp_key = ct.keyness(corp1_freq, corp2_freq, effect="log-ratio")
ct.head(corp_key, hits=10)


# N-grams
print("----")
corpus = texts
tokenized_trigram = ct.tokenize(corpus, lemma=False, ngram=3)
# don't lemmatize (assign inflected forms to their lexeme's citation form) because we want inflections to persist in ngram analysis
trigram_freq = ct.frequency(tokenized_trigram)
ct.head(trigram_freq, hits=10)


# Dependency bigrams
# note that dependency analysis uses call to nlp() function from Spacy, won't be applicable to minority language corpora
# bg_dict = ct.dep_bigram(corpus, "dobj")
# ct.head(bg_dict["bi_freq"], hits=10)
# ^^^ WARNING: MEMORY LEAK ^^^


# Strength of association
# uses bg_dict, omitting for now because of memory usage
# simil, omitting concordance

