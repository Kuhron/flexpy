import re


# global constants used in multiple places
PUNCTUATION_CHARS = [".", "?", "!", ",", "'", "\"", ";", ":", "-"]
WHITESPACE_CHARS = ["\n", "\t"]



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


def get_child_object(el, child_tag, rt_dict):
    child_el = get_single_child(el, child_tag)
    child_class = get_tag_class(child_el)
    # initialize it
    rt = child_el
    return child_class(rt, rt_dict)


def get_tag_class_name(el):
    if el.tag == "rt":
        class_name = "Rt{}".format(el.attrib["class"])
    elif el.tag == "objsur":
        raise Exception("shouldn't be getting tag class for object surrogates")
    else:
        class_name = el.tag
    return class_name


def get_tag_class(el):
    class_name = get_tag_class_name(el)
    import_flexpy_tags = __import__("flexpy").tags
    class_object = getattr(getattr(import_flexpy_tags, class_name), class_name)
    return class_object


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


def get_top_n_dict_items(dct, n):
    return sorted(dct.items(), key=lambda kv: kv[1], reverse=True)[:n]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def convert_whitespace_to_spaces(s):
    for c in WHITESPACE_CHARS:
        s = s.replace(c, " ")
    return s


# from Corpus Linguistics Homework 4, professor Kris Kyle
def add_space_before_punctuation(s):
    for c in PUNCTUATION_CHARS:
        new = " " + c + " "  # doing it on both sides because I got some tokens with leading commas like ",very"
        s = s.replace(c, new)
    return s


# from Corpus Linguistics Homework 4, professor Kris Kyle
def filter_split_token_list(lst):
    ignore_strs = [""] + PUNCTUATION_CHARS
    return [x for x in lst if x not in ignore_strs]  # return the list except anything in ignore_strs


# from Corpus Linguistics Homework 4, professor Kris Kyle
def tokenize_single_text(text_str):
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
    # corpus_str_lst is a list of strings
    # tokenize each string (text) individually, map this over the corpus_str_lst
    return [tokenize_single_text(text_str) for text_str in corpus_str_lst]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def lemmatize_single_text(text_lst, lemma_dict):
    # for each word in the text (which is a list of strings),
    # replace with the value in lemma_dict if the word is a key, else just use the word itself
    return [lemma_dict.get(word, word) for word in text_lst]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def lemmatize_corpus(tokenized_corpus, lemma_dict):
    # tokenized_corpus is a list of lists
    # each element in top-level list is a "tokenized text"
    # each tokenized text is a list of strings
    # run that list of strings through the single-text lemmatization function to replace words with their lemmata, if applicable
    return [lemmatize_single_text(tokenized_text, lemma_dict) for tokenized_text in tokenized_corpus]


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_frequency_dict_from_text_lst(text_lst, existing_d=None):
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
def get_frequency_dict_from_tokenized(tokenized):
    # whether it is lemmatized or not doesn't matter for the sake of the logic in this function
    # as the structure of lemmatized and non-lemmatized corpus is the same as long as it is tokenized
    frequency_dict = {}
    for text_lst in tokenized:
        frequency_dict = get_frequency_dict_from_text_lst(text_lst, existing_d=frequency_dict)
    return frequency_dict


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_rid_of_unicode_problems(byte_str):
    assert type(byte_str) is bytes, "expected bytes, got {}".format(type(byte_str))
    problem_bytes = [b"\x81", b"\x82"]
    for b in problem_bytes:
        byte_str = byte_str.replace(b, b"")
    return byte_str


# from Corpus Linguistics Homework 4, professor Kris Kyle
def get_corpus(corpus_dir):
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
    with open(lemma_dict_fp, "rb") as f:
        return pickle.load(f)


# from Corpus Linguistics Homework 4, professor Kris Kyle
def write_freq_dict_to_file(d, fp):
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
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    return re.sub('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))', r'_\1', s).lower()
