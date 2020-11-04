# intent here is to show the dependencies among the different element types in the FLEx data


import os
from flexpy.FlexPyUtil import get_tag_class_name


def create_dependency_dict(root, by_guid):
    # special types are <rt> and <objsur> (object surrogate), else just refer to it as its tag

    dependency_dict = {}

    all_elements = get_all_children_recursive(root)
    for el in all_elements:
        dependency_dict = add_element_to_dependency_dict(el, dependency_dict, by_guid)

    # sort the value sets into lists
    for k, parent_child_dict in dependency_dict.items():
        for parent_child, v in parent_child_dict.items():
            dependency_dict[k][parent_child] = sorted(v)
    return dependency_dict


def print_dependency_dict(root, by_guid):
    d = create_dependency_dict(root, by_guid)
    keys = sorted(d.keys())
    for k in keys:
        owners = d[k]["owners"]
        parents = d[k]["parents"]
        children = d[k]["children"]
        print("- {}".format(k))
        for owner_tag in owners:
            print("  <owner> {}".format(owner_tag))
        for parent_tag in parents:
            print("  <parent> {}".format(parent_tag))
        for child_tag in children:
            print("  <child> {}".format(child_tag))


def create_class_definition(el, dependency_dict):
    if el.tag == "rt":
        return create_rt_class_definition(el, dependency_dict)
    else:
        raise NotImplementedException(el.tag)


def create_tag_class_file(el, dependency_dict):
    this_dir_path = os.path.dirname(os.path.realpath(__file__))  # flexpy dir within flexpy repo
    tag_class_files_location = os.path.join(this_dir_path, "tags/")
    class_name = get_tag_class_name(el)
    tag_class_filename = "{}.py".format(class_name)
    tag_class_fp = os.path.join(tag_class_files_location, tag_class_filename)
    if os.path.exists(tag_class_fp):
        print("can't overwrite tag class; skipping; please delete manually if you want to rewrite: {}".format(tag_class_fp))
    else:
        class_definition_code = create_class_definition(el, dependency_dict)
        with open(tag_class_fp, "w") as f:
            f.write(class_definition_code)


def create_rt_class_definition(el, dependency_dict):
    assert el.tag == "rt"
    text_ignores = ["\n"]  # most or all of the rts seem to have text of "\n", which can just be ignored
    text_warnings = []
    if el.text is not None:
        warn_str = "rt {} with guid={} has text {}".format(el, el.attrib["guid"], repr(el.text))
        if el.text in text_ignores:
            pass
        elif el.text in text_warnings:
            # don't crash for these known cases
            print(warn_str)
        else:
            raise Exception(warn_str)

    long_class_name = get_tag_class_name(el)
    
    import_header = "from flexpy.Rt import Rt\n"
    import_header += "from flexpy.FlexPyUtil import get_child_object\n"
    import_header += "\n"
    class_header = "class {}(Rt):\n".format(long_class_name)
    init_header = "    def __init__(self, rt, rt_dict):\n"
    init_header += " "*8 + "super().__init__(rt, rt_dict)\n"
    init_vars_str = ""
    for child_el in el:
        child_tag = child_el.tag
        init_var_line = " "*8 + "self.{0} = get_child_object(self.rt, \"{0}\", self.rt_dict)".format(child_tag)
        init_vars_str += init_var_line + "\n"

    full_str = import_header + class_header + init_header + init_vars_str
    return full_str


def get_all_children_recursive(el):
    # make a flat list of all children, children of children, etc.
    children = []
    first_level_children = list(el)
    children += first_level_children
    for child in children:
        children += get_all_children_recursive(child)
    return children


def add_element_to_dependency_dict(el, dependency_dict, by_guid):
    if el.tag == "objsur":
        # don't add these, they should only be shown as children
        return dependency_dict
    tag_key = get_tag_key_from_element(el, by_guid)
    if tag_key not in dependency_dict:
        dependency_dict[tag_key] = {"parents": set(), "children": set(), "owners": set()}
    child_elements = list(el)  # this is how etree gets them, just uses __iter__
    child_tags = {get_tag_key_from_element(x, by_guid) for x in child_elements}
    dependency_dict[tag_key]["children"] |= child_tags

    # this way misses the fact that the objsur is under a tag telling what relationship it has (e.g. "Meanings")
    if "ownerguid" in el.attrib:
        owner_element = by_guid[el.attrib["ownerguid"]]
        owner_element_tag_key = get_tag_key_from_element(owner_element, by_guid)
        dependency_dict[tag_key]["owners"] |= {owner_element_tag_key}

    # add the parent dependencies, where this element is those children's parent
    for child_tag in child_tags:
        if child_tag not in dependency_dict:
            dependency_dict[child_tag] = {"parents": set(), "children": set(), "owners": set()}
        dependency_dict[child_tag]["parents"] |= {tag_key}

    return dependency_dict


def get_tag_key_from_element(el, by_guid):
    # rt should indicate its class attribute
    if el.tag == "rt":
        tag_key = "rt.{}".format(el.attrib["class"])

    # objsur should indicate its reference type (r=reference, o=ownership) and the type of the object referred to
    elif el.tag == "objsur":
        ref_letter = el.attrib["t"]
        if ref_letter == "r":
            ref_type = "ref"
        elif ref_letter == "o":
            ref_type = "own"
        else:
            raise ValueError("unknown objsur reference type: {} in element {}".format(ref_letter, el))

        element_referred_to = by_guid[el.attrib["guid"]]
        obj_tag = get_tag_key_from_element(element_referred_to, by_guid)
        tag_key = "{}.{}".format(ref_type, obj_tag)

    else:
        tag_key = el.tag

    return tag_key

