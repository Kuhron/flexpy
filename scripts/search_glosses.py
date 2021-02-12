from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon

project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"
bongu_corpus = Corpus(project_dir, project_name, include_punctuation=False)
contents = bongu_corpus.get_tokenized_contents()

regex = r"\b(eat|drink|kaikai|dring)"
# regex = r"\.ss"
# regex = r"^(to )?(eat|drink|kaikai|dring(im)?)$"
words = bongu_corpus.search_lexicon_glosses(regex)
print("searched for words containing gloss regex {}".format(regex))
print("Results: {}".format(words))

# print("searching in word glosses of texts")
# TODO
# words2 = bongu_corpus.search_word_glosses(regex)
# print("Results: {}".format(words2))

# print("searching in free translations of texts")
# TODO
# lines = bongu_corpus.search_free_translations(regex)
# print("Results: {}".format(lines))
