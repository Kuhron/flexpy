from flexpy.Corpus import Corpus


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "IxpantepecMixtec"

corpus = Corpus(project_dir, project_name, include_punctuation=False)

# desired result:
# list of lexical items, each place it occurs in 1st position
# and each place it occurs in 2nd position
# show baseline tone pattern and perturbed tone pattern of both
# look at this big list to see what jumps out

for text in corpus.texts:
    print(f"current text is {text}")
    