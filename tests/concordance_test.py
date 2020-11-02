# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.Corpus import Corpus
import flexpy.CorpusAnalysis as corp


if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)
    contents = corpus.get_tokenized_contents()

    sorting_indices = [-1, 1]  # sort by previous word, then next word
    corpus.print_concordance("ande", 50, sorting_indices)
