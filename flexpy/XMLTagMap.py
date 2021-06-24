"""A script containing functions which make it possible to show the dependencies 
among the different element types in the FLEx data.
"""


import os
from flexpy.FlexPyUtil import get_tag_class_name, get_element_info_str

from xml.etree import ElementTree as ET


def create_dependency_dict_from_single_root(root, by_guid):
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


def create_dependency_dict_from_multiple_roots(roots, by_guid):
    d = {}
    for root in roots:
        d.update(create_dependency_dict_from_single_root(root, by_guid))
        # what is the chance of guid collision among different projects? hopefully low
    return d


def print_dependency_dict(d):
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


def create_tag_class_file(el, dependency_dict):
    """Used to generate the files in `flexpy.tags`.
    """
    this_dir_path = os.path.dirname(os.path.realpath(__file__))  # flexpy dir within flexpy repo
    tag_class_files_location = os.path.join(this_dir_path, "tags/")
    class_name = get_tag_class_name(el)
    tag_class_filename = "{}.py".format(class_name)
    tag_class_fp = os.path.join(tag_class_files_location, tag_class_filename)
    init_fp = os.path.join(tag_class_files_location, "__init__.py")
    if not os.path.exists(init_fp):
        with open(init_fp, "w") as f:
            pass  # leave it blank
    if os.path.exists(tag_class_fp):
        print("can't overwrite tag class; skipping; please delete manually if you want to rewrite: {}".format(tag_class_fp))
    else:
        class_definition_code = create_tag_class_definition(el, dependency_dict)
        # print("\nTODO after debugging, uncomment code")
        # print("would write to fp: {}".format(tag_class_fp))
        # print("code:")
        # print(class_definition_code)
        # input("\n--- press enter to continue ---\n")
        with open(tag_class_fp, "w") as f:
            f.write(class_definition_code)


def create_tag_class_files(tag_dict):
    """Used to generate the files in `flexpy.tags`.
    """
    dependency_dict = tag_dict.dependency_dict
    for class_name, el_lst in tag_dict.by_tag.items():
        # get an element with this tag key
        el = el_lst[0]
        create_tag_class_file(el, dependency_dict)


def create_tag_class_definition(el, dependency_dict):
    """Used to generate the files in `flexpy.tags`.
    """
    if el.tag == "rt":
        text_ignores = ["\n"]  # most or all of the rts seem to have text of "\n", which can just be ignored
        text_warnings = []  # if see text in this list, warn the user
        if el.text is not None:
            warn_str = "element {} with guid={} has text {}".format(el, el.attrib.get("guid"), repr(el.text))
            if el.text in text_ignores:
                pass
            elif el.text in text_warnings:
                # don't crash for these known cases
                print(warn_str)
            else:
                raise Exception(warn_str)

    long_class_name = get_tag_class_name(el)

    import_header = ""
    if el.tag == "rt":
        import_header += "from flexpy.Rt import Rt\n"
    import_header += "from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects\n"
    import_header += "\n"

    if el.tag == "rt":
        class_header = "class {}(Rt):\n".format(long_class_name)
    else:
        class_header = "class {}:\n".format(long_class_name)

    # need params to be separated from preceding description by a blank line
    docstring_header = \
        " "*4 + f"\"\"\"A class for FLEx XML elements with the tag {el.tag}\n\n" +\
        " "*4 + ":param el: the `xml.etree.ElementTree.Element` object\n" +\
        " "*4 + ":param tag_dict: the `TagDict` object organizing the Elements in the FLEx project\n" +\
        " "*4 + "\"\"\"\n"

    init_header = "    def __init__(self, el, tag_dict):\n"
    if el.tag == "rt":
        init_header += " "*8 + "super().__init__(el, tag_dict)\n"
    init_header += " "*8 + "self.el = el\n"
    init_header += " "*8 + "self.tag_dict = tag_dict\n"
    init_header += " "*8 + "self.text = self.el.text\n"

    init_vars_str = ""
    if el.tag == "rt":
        # don't add the attribs because the Rt object will have them
        pass
    else:
        for attrib_key in dependency_dict[long_class_name]["attributes"]:
            init_vars_str += " "*8 + "self.{0} = self.el.attrib.get(\"{0}\")\n".format(attrib_key)

    getter_strs = [""]  # want blank lines between init and other methods
    ordered_child_getter_str = " "*4 + "def get_ordered_child_objects(self):\n"
    ordered_child_getter_str += " "*8 + "\"\"\"Gets the child objects of this element, in their order of appearance in the FLEx XML\"\"\"\n"
    ordered_child_getter_str += " "*8 + "return get_ordered_child_objects(self.el, self.tag_dict)\n"
    getter_strs.append(ordered_child_getter_str)

    for child_tag_short, child_tag_long, child_class_name in dependency_dict[long_class_name]["children"]:
        # init_var_line = " "*8 + "self.{0} = get_child_object(self.el, \"{1}\", self.tag_dict".format(child_tag_long, child_tag_short)
        getter_str = " "*4 + "def {0}(self):\n".format(child_tag_long)
        getter_str += " "*8 + f"\"\"\"Gets the child objects which have short tag of `{child_tag_short}`, long tag of `{child_tag_long}`"
        if child_class_name is not None:
            getter_str += f", class name of `{child_class_name}`"
        getter_str += "\"\"\"\n"
        getter_str += " "*8 + "return get_child_object(self.el, \"{0}\", self.tag_dict".format(child_tag_short)
        if child_class_name is not None:
            getter_str += ", class_name=\"{0}\"".format(child_class_name)
        getter_str += ")\n"
        getter_strs.append(getter_str)

    full_str = import_header + class_header + docstring_header + init_header + init_vars_str + "\n".join(getter_strs)
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
    assert type(el) is ET.Element, el
    if el.tag == "objsur":
        # don't add these, they should only be shown as children
        return dependency_dict
    
    get_empty_sub_dict = lambda: {"parents": set(), "children": set(), "owners": set(), "attributes": set()}
    tag_key = get_tag_key_from_element(el, by_guid)
    if tag_key not in dependency_dict:
        dependency_dict[tag_key] = get_empty_sub_dict()
    
    child_elements = list(el)  # this is how etree gets them, just uses __iter__
    child_tags = set()
    for child_el in child_elements:
        if child_el.tag == "rt":
            child_tag_short = "rt"
            child_class_name = child_el.attrib["class"]
            child_tag_long = get_tag_key_from_element(child_el, by_guid)
        elif child_el.tag == "objsur":
            reference_guid = child_el.attrib["guid"]
            referents = by_guid[reference_guid]

            child_tag_short = None
            for referent in referents:
                this_child_tag_short = referent.tag
                if child_tag_short is None:
                    child_tag_short = this_child_tag_short
                else:
                    assert this_child_tag_short == child_tag_short, f"mismatch in child_tag_short: {this_child_tag_short} vs {child_tag_short}"

            if child_tag_short == "rt":
                child_class_name = referent.attrib["class"]
            else:
                child_class_name = None
            child_tag_long = get_tag_key_from_element(child_el, by_guid)
            
            child_tag_from_referent = None
            for referent in referents:
                this_child_tag_from_referent = get_tag_key_from_element(referent, by_guid)
                if child_tag_from_referent is None:
                    child_tag_from_referent = this_child_tag_from_referent
                else:
                    assert this_child_tag_from_referent == child_tag_from_referent, f"mismatch in child_tag_from_referent: {this_child_tag_from_referent} vs {child_tag_from_referent}"
                    
            assert child_tag_long == child_tag_from_referent, "objsur tag key creation mismatch: {} from objsur, {} from referent".format(child_tag_long, child_tag_from_referent)
            
        else:
            child_tag_short = child_el.tag
            child_tag_long = child_el.tag  # short and long tag names are the same
            child_class_name = None
        tup = (child_tag_short, child_tag_long, child_class_name)
        child_tags.add(tup)

    dependency_dict[tag_key]["children"] |= child_tags

    # attribute names may have been expanded by ET.parse if they contained namespaces
    # if we attempt to create self.{attrib_key} like this, we will get a SyntaxError
    # so assert that no such attributes exist
    # this can be ensured by using FlexPyUtil.parse_xml_without_namespaces()
    attribute_names = set(el.attrib.keys())
    if any("}" in x for x in attribute_names):
        el_str = get_element_info_str(el)
        raise Exception(f"tag_key {tag_key} has namespace URL in an attribute key:\n{el_str}")
    dependency_dict[tag_key]["attributes"] |= attribute_names

    # this way misses the fact that the objsur is under a tag telling what relationship it has (e.g. "Meanings")
    if "ownerguid" in el.attrib:
        owner_elements = by_guid[el.attrib["ownerguid"]]
        owner_element_tag_key = None
        for owner_element in owner_elements:
            this_owner_element_tag_key = get_tag_key_from_element(owner_element, by_guid)
            if owner_element_tag_key is None:
                owner_element_tag_key = this_owner_element_tag_key
            else:
                assert this_owner_element_tag_key == owner_element_tag_key, f"mismatch in owner_element_tag_key: {this_owner_element_tag_key} vs {owner_element_tag_key}"
        dependency_dict[tag_key]["owners"] |= {owner_element_tag_key}

    # add the parent dependencies, where this element is those children's parent
    for child_tag_short, child_tag_long, child_class_name in child_tags:
        if child_tag_long not in dependency_dict:
            dependency_dict[child_tag_long] = get_empty_sub_dict()
        dependency_dict[child_tag_long]["parents"] |= {tag_key}

    return dependency_dict


def get_tag_key_from_element(el, by_guid):
    """Used to get the tag_key (which is used to find elements in a `TagDict`)
    for a given element.

    :param el:
    :type el: xml.etree.ElementTree.Element
    :param by_guid: the dictionary of elements by their guid, used to find tags of parents of this element
    :type by_guid: dict
    """
    # rt should indicate its class attribute
    assert type(el) is ET.Element, el
    if el.tag == "rt":
        tag_key = "Rt{}".format(el.attrib["class"])

    # objsur should indicate its reference type (r=reference, o=ownership) and the type of the object referred to
    elif el.tag == "objsur":
        # ref_letter = el.attrib["t"]
        # if ref_letter == "r":
        #     ref_type = "ref"
        # elif ref_letter == "o":
        #     ref_type = "own"
        # else:
        #     raise ValueError("unknown objsur reference type: {} in element {}".format(ref_letter, el))

        elements_referred_to = by_guid[el.attrib["guid"]]
        obj_tag = None
        for element_referred_to in elements_referred_to:
            this_obj_tag = get_tag_key_from_element(element_referred_to, by_guid)
            if obj_tag is None:
                obj_tag = this_obj_tag
            else:
                assert obj_tag == this_obj_tag, f"mismatched obj_tags: {this_obj_tag} vs {obj_tag}"
        # tag_key = "{}.{}".format(ref_type, obj_tag)
        tag_key = obj_tag

    else:
        tag_key = el.tag

    return tag_key

