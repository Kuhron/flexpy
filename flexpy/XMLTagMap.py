# intent here is to show the dependencies among the different element types in the FLEx data


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

