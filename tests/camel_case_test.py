# test the function which converts camel case to snake case

from flexpy.Corpus import Corpus
from flexpy.FlexPyUtil import camel_case_to_snake_case


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"
bongu_corpus = Corpus(project_dir, project_name, include_punctuation=False)

print("testing camel case function on all rt classes in the database")
conversions = {}
for rt in bongu_corpus.tag_dict.get_all_rts():
    tag = rt.attrib["class"]
    new_tag = camel_case_to_snake_case(tag)
    if tag in conversions:
        assert new_tag == conversions[tag], "mismatched conversion: {} -> {} + {}".format(tag, conversions[tag], new_tag)
    else:
        conversions[tag] = new_tag

for tag, new_tag in sorted(conversions.items()):
    print("{} -> {}".format(tag, new_tag))

print("success")
