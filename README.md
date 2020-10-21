# flexpy

Python API for working with SIL FieldWorks Language Explorer (FLEx) databases. Some web scraping of Papuan Bible translations is also in here. Better organization and more features to come.

Install with:

    pip install flexpy

#### Example usage
    from flexpy.Corpus import Corpus
    
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    project_name = "Bongu"
    bongu_corpus = Corpus(project_dir, project_name)
    contents = bongu_corpus.get_tokenized_contents()  # already tokenized
    
    # now you can run statistics on contents

