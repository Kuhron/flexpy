from flexpy.Corpus import Corpus

project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"
bongu_corpus = Corpus(project_dir, project_name)
contents = bongu_corpus.get_tokenized_contents()

print("dependencies in the XML:")
bongu_corpus.rt_dict.print_dependency_dict()

print("success")
