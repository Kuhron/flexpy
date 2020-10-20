def get_single_child(element, child_tag):
    children = element.findall(child_tag)
    if len(children) == 1:
        return children[0]
    elif len(children) == 0:
        return None
    error_str = "not one {} was found, but {}:\n".format(child_tag, len(children))
    for child in children:
        error_str += get_element_info_str(child) + "\n"
    error_str += "in parent:\n{}".format(get_element_info_str(element))
    raise Exception(error_str)


def get_element_info_str(element):
    s = ""

    begin_tag_info = "<{} ".format(element.tag)
    guid_info = "guid={}> ".format(element.attrib.get("guid"))
    s += begin_tag_info + guid_info

    attributes_info = "element with attributes:\n  {}\n".format(element.attrib)
    text_info = "and text:\n  {}\n".format(repr(element.text))  # repr so we can still see if it's an empty string or what
    end_tag_info = "</{}>\n".format(element.tag)
    s += attributes_info + text_info + end_tag_info
    return s
