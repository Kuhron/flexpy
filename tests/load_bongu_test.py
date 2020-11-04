import random

from flexpy.Corpus import Corpus
import flexpy.XMLTagMap as xml_tag_map


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"
bongu_corpus = Corpus(project_dir, project_name)
contents = bongu_corpus.get_tokenized_contents()

print("dependencies in the XML:")
dependency_dict = bongu_corpus.rt_dict.create_dependency_dict()
bongu_corpus.rt_dict.print_dependency_dict()

random_rt = random.choice(list(bongu_corpus.rt_dict.values()))
print("class definition for {}".format(random_rt.attrib["class"]))
print(xml_tag_map.create_class_definition(random_rt, dependency_dict))
# xml_tag_map.create_tag_class_file(random_rt, dependency_dict)

bongu_corpus.rt_dict.create_tag_class_files(dependency_dict)



print("success")
