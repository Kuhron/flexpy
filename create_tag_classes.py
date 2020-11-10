from flexpy.TagDict import TagDict
from flexpy.FlexPyUtil import create_tag_class_files


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "Bongu"

# create the tag classes
tag_dict = TagDict.from_project_dir_and_name(project_dir, project_name)
create_tag_class_files(tag_dict)
