# Kris's library
from corpus_toolkit import corpus_tools as ct

# FlexPy-specific classes
from flexpy.Corpus import Corpus
from flexpy.RtDict import RtDict
from flexpy.Text import Text

import flexpy.CorpusAnalysis as corp


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
    corpus = Corpus(project_dir, project_name)
    contents = corpus.get_contents()

    print("corpus size: {}".format(corp.get_corpus_size_words(contents)))
    # report_frequencies_naive(contents)
    corp.perform_kris_analysis(contents)
