import random

from flexpy.Corpus import Corpus
import flexpy.XMLTagMap as xml_tag_map


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"

bongu_corpus = Corpus(project_dir, project_name, include_punctuation=False)
contents = bongu_corpus.get_tokenized_contents()

dependency_dict = bongu_corpus.tag_dict.dependency_dict

random_rt = random.choice(bongu_corpus.tag_dict.all_elements())
print("\n-- class definition for {}".format(random_rt.attrib["class"]))
print(xml_tag_map.create_tag_class_definition(random_rt, dependency_dict))

# test instantiating a tag class from an element
dict_of_single_class = bongu_corpus.tag_dict["RtCmAnnotationDefn"]
random_guid = random.choice(list(dict_of_single_class.keys()))
els_with_guid = dict_of_single_class[random_guid]
el = els_with_guid[0]
print("\n-- attempting object instantiation from element {}".format(el))
obj = bongu_corpus.tag_dict.get_python_object_from_element(el)
print(obj)
print(obj.__dict__)

print("success")
