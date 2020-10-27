from flexpy.Corpus import Corpus
from flexpy.Lexicon import Lexicon

project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"
bongu_corpus = Corpus(project_dir, project_name)
contents = bongu_corpus.get_tokenized_contents()

regex = r"eat|drink|kaikai|dring"
words = bongu_corpus.lexicon.search_glosses(regex)
print("searched for words containing gloss regex {}".format(regex))
print("Results: {}".format(words))

