from flexpy.Corpus import Corpus

project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bara"
corpus = Corpus(project_dir, project_name, include_punctuation=True)

output_dir = "/home/wesley/Desktop/UOregon Work/CorpusLinguistics/corpora/Bara/"
corpus.write_texts_to_file(output_dir)
