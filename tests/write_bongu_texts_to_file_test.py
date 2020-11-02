from flexpy.Corpus import Corpus

project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"
bongu_corpus = Corpus(project_dir, project_name)

output_dir = "/home/wesley/Desktop/UOregon Work/CorpusLinguistics/corpora/Bongu/"
bongu_corpus.write_texts_to_file(output_dir)
