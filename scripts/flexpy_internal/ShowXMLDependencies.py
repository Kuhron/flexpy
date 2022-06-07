from flexpy.TagDict import TagDict


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "IxpantepecMixtec"

# create the tag classes
tag_dict = TagDict.from_project_dir_and_name(project_dir, project_name)

print("\n-- dependencies in the XML:")
tag_dict.print_dependency_dict()

print("\n-- dependency dict keys (all element tags):")
print(sorted(tag_dict.dependency_dict.keys()))
