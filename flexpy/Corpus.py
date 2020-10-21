from flexpy.RtDict import RtDict
from flexpy.Text import Text

from flexpy.FlexPyUtil import tokenize_single_text



class Corpus:
    def __init__(self, project_dir, project_name):
        self.project_dir = project_dir
        self.project_name = project_name
        self.texts = self.get_texts()
        self.contents = self.get_contents()

    def get_texts(self):
        flex_dir = self.project_dir + "{}/".format(self.project_name)
        fp = flex_dir + "{}.fwdata".format(self.project_name)
        # print("getting corpus from FLEx project {} at {}".format(self.project_name, fp))
        rt_dict = RtDict.from_fwdata_file(fp)
    
        texts = rt_dict.get_texts()
        return texts

    def get_contents(self):
        contents_lst = []
        for text in self.texts:
            # print("----")
            # print(text)
            contents = text.get_contents()
            # print(contents)
            contents_lst += contents
            # print("----\n")
        return contents_lst

    def get_tokenized_contents(self):
        # treats the whole corpus as a single text for now
        result = []
        for s in self.contents:
            result += tokenize_single_text(s)
        return result
