"""A script containing various useful functions.
"""

import re
from io import StringIO
import xml.etree.ElementTree as ET


# global constants used in multiple places
PUNCTUATION_CHARS = [".", "?", "!", ",", "'", "\"", ";", ":", "-"]
WHITESPACE_CHARS = ["\n", "\t"]



def get_single_child(element, child_tag):
    """Gets the only child of an XML element with tag `child_tag`.
    If there is exactly one such child, returns it.
    If there are no such children, returns `None`.
    If there are more than one such child, throws an error.
    """
    assert type(element) is ET.Element, "invalid element: {}".format(element)
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


def get_children(element, child_tag):
    """Gets all children, with a certain tag, of an XML element.
    Identical to `element.findall()`.
    """
    return element.findall(child_tag)


def get_ordered_child_objects(el, tag_dict):
    """For `objsur` elements only. Gets ordered list of child elements as Python objects,
    i.e., classes found in `flexpy.tags`.
    """
    # for objsurs only
    assert type(el) is ET.Element, "invalid element: {}".format(el)
    child_objects = []
    for child_el in el:
        if child_el.tag == "objsur":
            child_object = tag_dict.get_python_object_from_element(child_el)
            child_objects.append(child_object)
    return child_objects


def get_child_object(el, child_tag, tag_dict, class_name=None):
    """Gets a Python object, i.e., a class found in `flexpy.tags` specific to the
    tag of the child element.
    """
    assert type(el) is ET.Element, "invalid element: {}".format(el)
    if class_name is not None:
        assert child_tag == "rt", "can't pass class_name for anything other than rt child"
    if child_tag == "rt":
        assert class_name is not None, "can't omit class_name for rt child"

    el_has_objsurs = el.find("objsur") is not None
    if el_has_objsurs:
        # shouldn't have anything else
        assert all(child_el.tag == "objsur" for child_el in el), "el {} has objsurs as well as other child tags".format(el)
        # we will then search for objsurs which meet the criteria
        # we should return a list of these
        matching_referent_els = []
        for objsur in el:
            reference_guid = objsur.attrib["guid"]
            referents = tag_dict[reference_guid]
            for referent in referents:
                if referent.tag == child_tag:
                    if referent.tag == "rt":
                        matches = referent.attrib["class"] == class_name
                    else:
                        matches = True
                else:
                    matches = False
                if matches:
                    referent_object = tag_dict.get_python_object_from_element(referent)
                    matching_referent_els.append(referent_object)
        return matching_referent_els
    elif child_tag in ["AUni", "AStr", "Run"]:
        # there can be many of these for different writing systems
        # create a dict from writing system to AUni tag
        children_els = el.findall(child_tag)
        return [tag_dict.get_python_object_from_element(child_el) for child_el in children_els]
    else:
        # there should only be one of each child type
        child_el = get_single_child(el, child_tag)
        if child_el is None:
            return None
        return tag_dict.get_python_object_from_element(child_el)


def get_tag_class_name(el):
    """Gets the class name for the Python object corresponding to an XML element type.
    
    <rt class="Xyz"> will give "RtXyz", corresponding to the class
    `flexpy.tags.RtXyz.RtXyz`.
    
    <objsur> elements have no such class; the referred object should be the element whose class is being created.

    All other tags have a class name identical to their tag; for instance, <AUni> elements
    correspond to the class `flexpy.tags.AUni.AUni`.
    """
    if el.tag == "rt":
        class_name = "Rt{}".format(el.attrib["class"])
    elif el.tag == "objsur":
        raise Exception("shouldn't be getting tag class for object surrogates")
    else:
        class_name = el.tag
    return class_name


def get_tag_class(el):
    """Gets the actual class, as a Python object, corresponding to an XML element in FLEx.
    This class object may then be instantiated. This is done in constructing a `TagDict`.
    """
    class_name = get_tag_class_name(el)
    # see https://docs.python.org/3/library/functions.html#__import__
    from_x = "flexpy.tags." + class_name
    class_object = getattr(__import__(from_x, fromlist=[class_name]), class_name)
    return class_object


def get_element_info_str(element):
    """Gets a readable string containing information about an XML element,
    including attributes and guid.
    """
    s = ""

    begin_tag_info = "<{} ".format(element.tag)
    guid_info = "guid={}> ".format(element.attrib.get("guid"))
    s += begin_tag_info + guid_info

    attributes_info = "element with attributes:\n  {}\n".format(element.attrib)
    text_info = "and text:\n  {}\n".format(repr(element.text))  # repr so we can still see if it's an empty string or what
    end_tag_info = "</{}>\n".format(element.tag)
    s += attributes_info + text_info + end_tag_info
    return s


def get_top_n_dict_items(dct, n):
    """Gets the `n` keys in `dct` which have the highest values.
    """
    return sorted(dct.items(), key=lambda kv: kv[1], reverse=True)[:n]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def convert_whitespace_to_spaces(s):
    """Replaces all whitespace characters in `s` with a single space.
    """
    for c in WHITESPACE_CHARS:
        s = s.replace(c, " ")
    return s


# from Corpus Linguistics Homework 4, professor Kris Kyle
def add_space_before_punctuation(s):
    """For tokenization of a text. Adds a single space on each side of every punctuation character.
    """
    for c in PUNCTUATION_CHARS:
        new = " " + c + " "  # doing it on both sides because I got some tokens with leading commas like ",very"
        s = s.replace(c, new)
    return s


# from Corpus Linguistics Homework 4, professor Kris Kyle
def filter_split_token_list(lst):
    """For tokenization of a text. Takes a list of tokens and returns
    all non-empty and non-punctuation tokens.
    """
    ignore_strs = [""] + PUNCTUATION_CHARS
    return [x for x in lst if x not in ignore_strs]  # return the list except anything in ignore_strs


# from Corpus Linguistics Homework 4, professor Kris Kyle
def tokenize_single_text(text_str):
    """Tokenizes a single string which contains an entire text.
    Removes whitespace and punctuation.
    """
    # pre-process by getting rid of case, replacing whitespace, and separating punctuation from preceding word
    text_str = text_str.lower()
    text_str = convert_whitespace_to_spaces(text_str)
    text_str = add_space_before_punctuation(text_str)

    # now split and filter unwanted tokens e.g. empty string
    text_lst = text_str.split()
    text_lst = filter_split_token_list(text_lst)
    return text_lst


# from Corpus Linguistics Homework 4, professor Kris Kyle
def tokenize_corpus(corpus_str_lst):
    """Tokenizes each of a list of strings. Each string is assumed to be an entire text.
    Returns a list of lists. First-level items are token lists for each text.
    """
    # corpus_str_lst is a list of strings
    # tokenize each string (text) individually, map this over the corpus_str_lst
    return [tokenize_single_text(text_str) for text_str in corpus_str_lst]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def lemmatize_single_text(text_lst, lemma_dict):
    """Lemmatizes an already-tokenized text according to `lemma_dict`,
    which should map from forms to their lemmas. If a form is not found,
    the lemma is assumed to be the form itself.
    """
    # for each word in the text (which is a list of strings),
    # replace with the value in lemma_dict if the word is a key, else just use the word itself
    return [lemma_dict.get(word, word) for word in text_lst]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def lemmatize_corpus(tokenized_corpus, lemma_dict):
    """Lemmatizes an entire already-tokenized corpus (list of lists).
    See `lemmatize_single_text()`.
    """
    # tokenized_corpus is a list of lists
    # each element in top-level list is a "tokenized text"
    # each tokenized text is a list of strings
    # run that list of strings through the single-text lemmatization function to replace words with their lemmata, if applicable
    return [lemmatize_single_text(tokenized_text, lemma_dict) for tokenized_text in tokenized_corpus]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_frequency_dict_from_text_lst(text_lst, existing_d=None):
    """Takes an already-tokenized text, returns a dictionary of token frequencies.

    :param text_lst:
    :param existing_d: a token frequency dictionary to add to, if provided
    """
    # can add to existing freq dict (useful for doing a whole corpus but one text at a time)
    # or if no existing dict is given, start from a blank dict
    # note that it is BAD practice to have a mutable default argument, e.g. def f(x, y={}), see https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
    d = existing_d if existing_d is not None else {}
    for word in text_lst:
        if word not in d:
            d[word] = 0
        d[word] += 1
    return d


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_frequency_dict_from_tokenized_corpus(tokenized):
    """Takes an already-tokenized corpus (list of tokenized texts),
    returns a token frequency dictionary.
    """
    # whether it is lemmatized or not doesn't matter for the sake of the logic in this function
    # as the structure of lemmatized and non-lemmatized corpus is the same as long as it is tokenized
    frequency_dict = {}
    for text_lst in tokenized:
        frequency_dict = get_frequency_dict_from_text_lst(text_lst, existing_d=frequency_dict)
    return frequency_dict


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_rid_of_unicode_problems(byte_str):
    """Takes a `bytes` object, removes it with certain problem bytes removed.
    """
    assert type(byte_str) is bytes, "expected bytes, got {}".format(type(byte_str))
    problem_bytes = [b"\x81", b"\x82"]
    for b in problem_bytes:
        byte_str = byte_str.replace(b, b"")
    return byte_str


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_corpus(corpus_dir):
    """Gets a corpus (list of text strings) from a directory containing .txt files.
    Each .txt file is assumed to correspond to a single text in the corpus.
    """
    strs = []
    for fp in glob.glob(corpus_dir + "/*.txt"):
        with open(fp, "rb") as f:
            contents = f.read()
        contents = get_rid_of_unicode_problems(contents)
        try:
            contents = contents.decode("utf-8")
        except UnicodeDecodeError:
            raise Exception("bad contents in file {}:\n{}".format(fp, contents))
        strs.append(contents)
    return strs


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_lemma_dict(lemma_dict_fp):
    """Loads a pickle object containing a lemmatization dictionary.
    """
    with open(lemma_dict_fp, "rb") as f:
        return pickle.load(f)


# from Corpus Linguistics Homework 4, professor Kris Kyle
def write_freq_dict_to_file(d, fp):
    """Writes a token frequency dictionary to file.
    """
    tups = sorted(d.items(), key=lambda kv: kv[1], reverse=True)  # my preferred syntax for getting dict keys by value in descending order
    header = "word\tfrequency"
    str_from_tup = lambda tup: "{}\t{}".format(*tup)  # quick helper function to get the formatted string from each key-value pair

    # scalable
    with open(fp, "w") as f:
        f.write(header)
        for tup in tups:
            this_str = str_from_tup(tup)
            f.write("\n" + this_str)


def get_pretty_concordance_formatting(conc_list, max_words_left, max_words_right):
    """Gets a readable concordance format in preparation for printing or writing to file.

    :param conc_list: the list of concordance lines. Data structure must be a list of
        lists. Each first-level list corresponds to a concordance line.
        Within each first-level list, expect three elements: list of words on left side,
        target word, list of words on right side.
    :param max_words_left: maximum number of words to include on the left side of the target
    :type max_words_left: int
    :param max_words_right: maximum number of words to include on the right side of the target
    :type max_words_right: int
    """
    lefts  = [" ".join(x[0][-max_words_left:]) for x in conc_list]
    targets = [x[1] for x in conc_list]
    rights = [" ".join(x[2][:max_words_right]) for x in conc_list]
    max_len_left  = max(len(x) for x in lefts)
    max_len_target = max(len(x) for x in targets)
    max_len_right = max(len(x) for x in rights)
    left_size = max(max_len_left + 1, len("left_context") + 1)
    target_size = max(max_len_target + 1, len("node_word") + 1)
    # don't need to add spaces to the right of the rightmost stuff
    return {
        "lefts": lefts,
        "targets": targets,
        "rights": rights,
        "left_size": left_size,
        "target_size": target_size,
    }


def print_concordance_pretty(conc_list, max_words_left, max_words_right):
    """Prints a list of concordance lines in readable format. See `get_pretty_concordance_formatting()`.
    """
    if len(conc_list) == 0:
        print("(no concordance found)")
        return
    formatting = get_pretty_concordance_formatting(conc_list, max_words_left, max_words_right)
    left_size = formatting["left_size"]
    target_size = formatting["target_size"]
    lefts = formatting["lefts"]
    targets = formatting["targets"]
    rights = formatting["rights"]

    header = "left_context".rjust(left_size) + " | " + "node_word".ljust(target_size) + "| " + "right_context"
    print(header)
    for left, target, right in zip(lefts, targets, rights):
        line = left.rjust(left_size) + " | " + target.ljust(target_size) + "| " + right
        print(line)


def write_concordance_pretty(fp, conc_list, max_words_left, max_words_right):
    """Writes a concordance list to file in readable format. See `get_pretty_concordance_formatting()`.
    """
    formatting = get_pretty_concordance_formatting(conc_list, max_words_left, max_words_right)
    left_size = formatting["left_size"]
    target_size = formatting["target_size"]
    lefts = formatting["lefts"]
    targets = formatting["targets"]
    rights = formatting["rights"]
    with open(fp, "w") as f:
        header = "left_context".rjust(left_size) + " | " + "node_word".ljust(target_size) + "| " + "right_context"
        f.write(header)
        for left, target, right in zip(lefts, targets, rights):
            line = left.rjust(left_size) + " | " + target.ljust(target_size) + "| " + right
            f.write("\n" + line)


def sort_concordance_list(conc_list, sorting_indices):
    """Sorts a concordance list.

    :param conc_list: a list of lists corresponding to concordance lines. 
        See `get_pretty_concordance_formatting()` for description of this format.
    :param sorting_indices: a list of ints which correspond to
        the positions of words in a concordance line. 0 means the target word.
        Negative indices mean words to the left. Positive indices mean words to the right.
        Thus, `sorting_indices` of [-1, 1, 0] would sort first by the word to the left of the target,
        then by the word to the right of the target, then by the target itself.
    """
    # sorting indices in order of priority
    # each index is number of words away from the token (can be negative for words before the token, and can be zero for the token)
    # assign a tuple of sort values to each item in the list
    d = {}
    for line in conc_list:
        left_words_lst, target, right_words_lst = line
        # go through the sorting indices to construct the tuple
        sort_vals = []
        for s_i in sorting_indices:
            # get the thing at this index in this line
            if s_i == 0:
                sort_val = target
            elif s_i > 0:
                try:
                    sort_val = right_words_lst[s_i-1]  # 1 corresponds to first word, index 0 of right list
                except IndexError:
                    sort_val = ""
            elif s_i < 0:
                try:
                    sort_val = left_words_lst[s_i]  # -1 corresponds to last word, index -1 of left lst
                except IndexError:
                    sort_val = ""
            else:
                raise ValueError("invalid sort index {}".format(s_i))
            sort_vals.append(sort_val)
        sort_vals_tup = tuple(sort_vals)
        d[sort_vals_tup] = line

    sorted_kvs = sorted(d.items())
    sorted_lines = [kv[1] for kv in sorted_kvs]
    return sorted_lines


def camel_case_to_snake_case(s):
    """Converts a CamelCase string to snake_case.
    """
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    return re.sub('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))', r'_\1', s).lower()


def get_strs_from_form(form):
    """Gets the strings from a FLEx `Form` element.
    Returns a dictionary of element type name to list of the text in such elements.

    For instance, a possible return value could be {"AStr": ["asdf", "aoeu"], "AUni": [], "Str": []},
    meaning that the FLEx `Form` element had two child elements of type `AStr`,
    containing the strings "asdf" and "aoeu", and no child elements with other string-like types.

    :param form: 
    :type form: flexpy.tags.Form.Form
    """
    assert form.__class__.__name__ == "Form", type(form)  # avoid circular import type checking

    # AStr has a Run child tag with the text
    astrs = form.AStr()
    if astrs is not None:
        astr_text = get_str_from_AStrs(astrs)
    else:
        astr_text = ""

    # AUni has text in tag
    aunis = form.AUni()
    if aunis is not None:
        auni_text = get_str_from_AUnis(aunis)
    else:
        auni_text = ""

    # Str has a Run child tag with the text
    strtags = form.Str()
    if strtags is not None:
        strtag_text = get_str_from_Strs(strtags)
    else:
        strtag_text = ""
    
    return {"AStr": astr_text, "AUni": auni_text, "Str": strtag_text}


def get_str_from_AStr(astr):
    strs = get_strs_from_AStr(astr)
    strs = [(s if s is not None else "") for s in strs]
    return "".join(strs)


def get_strs_from_AStr(astr):
    assert astr.__class__.__name__ == "AStr", type(astr)
    return [run.text for run in astr.Run()]


def get_str_from_AStrs(astrs):
    strs = [get_str_from_AStr(astr) for astr in astrs]
    return "".join(strs)


def get_strs_from_AStrs(astrs):
    return [get_strs_from_AStr(astr) for astr in astrs]


def get_str_from_AUni(auni):
    assert auni.__class__.__name__ == "AUni", type(auni)
    return auni.text

# get plural strs from singular AUni should not be possible

def get_str_from_AUnis(aunis):
    strs = [get_str_from_AUni(auni) for auni in aunis]
    return "".join(strs)


def get_strs_from_AUnis(aunis):
    return [get_strs_from_AUni(auni) for auni in aunis]


def get_str_from_Str(strtag):
    strs = get_strs_from_Str(strtag)
    return "".join(strs)


def get_strs_from_Str(strtag):
    return [run.text for run in strtag.Run()]


def get_str_from_Strs(strtags):
    strs = [get_str_from_Str(strtag) for strtag in strtags]
    return "".join(strs)


def get_strs_from_Strs(strtags):
    return [get_strs_from_Str(strtag) for strtag in strtags]


def get_strs_from_form_as_list(form):
    """Gets the strings contained in a FLEx `Form` element as a list,
    NOT in order of appearance.
    """
    forms_dict = get_strs_from_form(form)
    has_astr = forms_dict["AStr"] is not None and forms_dict["AStr"] != []
    has_auni = forms_dict["AUni"] is not None and forms_dict["AUni"] != []
    has_str = forms_dict["Str"] is not None and forms_dict["Str"] != []
    n_forms = has_astr + has_auni + has_str
    if n_forms == 0:
        print("warning: no valid strings found in form {}".format(form))
        return []
    # assert n_forms == 1, "forms_dict has != 1 valid forms: {}".format(forms_dict)
    forms = []
    for k, v in forms_dict.items():
        if v is not None:
            assert type(v) is str, v
            if v != "":
                forms.append(v)
    return forms


def get_unique_strs_from_form_as_list(form):
    """Gets the unique strings contained in a FLEx `Form` element.
    """
    forms = get_strs_from_form_as_list(form)
    return list(set(forms))


def get_single_str_from_form(form, allow_repeat=True):
    """Gets the single string contained in a FLEx `Form` element.
    If there are no strings, returns `None`.
    If there are more than one, raises an error.
    
    :param form: the `flexpy.tags.Form.Form` object corresponding to the XML element
    :param allow_repeat: (default `True`) Whether multiple occurrences of the same string (e.g.,
        if it shows up as both an `AStr` and an `AUni`) should be treated as a single string.
        If `allow_repeat` is `False` in a case where the same string appears more than once
        in the `Form` element, the function will raise an error.
    :type allow_repeat: bool
    """
    # allow_repeat: if multiple strs are there but they're all the same, allow it
    all_forms = get_strs_from_form_as_list(form)

    if len(all_forms) == 0:
        return None

    if allow_repeat:
        forms = list(set(all_forms))
        assert len(forms) == 1, "more than 1 form even when allowing repeat: {}".format(forms)
    else:
        assert len(all_forms) == 1, "more than 1 form: {}".format(all_forms)
        forms = all_forms
    return forms[0]


def parse_xml_with_namespaces(fp):
    """Normal XML parsing using `xml.etree.ElementTree`.
    """
    tree = ET.parse(fp)
    return tree.getroot()


def parse_xml_without_namespaces(fp):
    """XML parsing which strips out namespaces.
    See https://stackoverflow.com/questions/13412496/python-elementtree-module-how-to-ignore-the-namespace-of-xml-files-to-locate-ma
    
    This is included because some FLEx files have elements with attribute `xml:space`
    which indicates whether whitespace should be preserved, and this causes problems.
    """
    # As far as I am aware, removing the namespace from this `space` attribute will not
    # cause issues other than potentially having duplicate attributes, so check for that.

    # remove namespaces from tags
    it = ET.iterparse(fp)
    for _, el in it:
        _, _, el.tag = el.tag.rpartition('}')  # strip namespace from tag
        new_attrib = {}
        for k, v in el.attrib.items():
            _, _, new_k = k.rpartition('}')  # strip namespace from key in attribute dict
            assert new_k not in new_attrib, f"duplication of key {new_k} after stripping namespace; original key {k}"
            new_attrib[new_k] = v
        el.attrib = new_attrib
    root = it.root
    return root
