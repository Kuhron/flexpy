import random

from flexpy.Corpus import Corpus
from flexpy.FlexPyUtil import get_python_object_from_element
import flexpy.XMLTagMap as xml_tag_map


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"

bongu_corpus = Corpus(project_dir, project_name)
contents = bongu_corpus.get_tokenized_contents()

dependency_dict = bongu_corpus.tag_dict.create_dependency_dict()

random_rt = random.choice(list(bongu_corpus.tag_dict.values()))
print("class definition for {}".format(random_rt.attrib["class"]))
print(xml_tag_map.create_tag_class_definition(random_rt, dependency_dict))

# test instantiating a tag class from an element
el = list(bongu_corpus.tag_dict["CmAnnotationDefn"].values())[0]
obj = get_python_object_from_element(el, bongu_corpus.tag_dict)
print(obj)
print(obj.__dict__)


print("success")
