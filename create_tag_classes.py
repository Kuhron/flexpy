from flexpy.TagDict import TagDict
from flexpy.XMLTagMap import create_tag_class_files


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
# project_name = "Bongu"

# create the tag classes
# tag_dict = TagDict.from_project_dir_and_name(project_dir, project_name)
tag_dict = TagDict.from_all_projects_in_dir(project_dir)

# print("\n-- dependencies in the XML:")
# tag_dict.print_dependency_dict()

# print("\n-- dependency dict keys (all element tags):")
# print(sorted(tag_dict.dependency_dict.keys()))

input("press enter to begin creating class files")
create_tag_class_files(tag_dict)
