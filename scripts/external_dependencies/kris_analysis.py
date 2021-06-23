# Kris's library
from corpus_toolkit import corpus_tools as ct

# FlexPy-specific classes
from flexpy.Corpus import Corpus
from flexpy.TagDict import TagDict
from flexpy.Text import Text

import flexpy.CorpusAnalysis as corp


if __name__ == "__main__":
    config = {}
    # with open("FlexPyConfig.txt") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         line = line.strip()
    #         if len(line) == 0 or line[0] == "#":
    #             continue
    #         k, v = line.split("=")
    #         config[k.strip()] = v.strip()

    # project_name = config["project_name"]
    # project_dir = config["project_dir"]
    project_name = "Isan"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name, include_punctuation=False)
    contents = corpus.get_contents()

    print("corpus size: {}".format(corp.get_corpus_size_words(contents)))
    # report_frequencies_naive(contents)
    corp.perform_kris_analysis(contents)
