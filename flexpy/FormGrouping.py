from flexpy.WordForm import WordForm, WordFormMorpheme



def group_wordforms(tokenized, grouping_function):
    new_tokenized = []
    for text in tokenized:
        new_text = group_wordforms_in_text(text, grouping_function)
        new_tokenized.append(new_text)
    return new_tokenized


def group_wordforms_in_text(text, grouping_function):
    new_text = []
    for token in text:
        new_token = grouping_function(token)
        new_text.append(new_token)
    return new_text


def get_form_group_last_morpheme(wordform):
    assert type(wordform) is WordForm, wordform
    morph = wordform.morphemes[-1]
    morph_type = morph.morph_type
    form = morph.form
    if form is None:
        return "None"
    elif morph_type in [None, "None"]:
        return "None"
    elif morph_type in ["root", "stem", "particle", "phrase"]:
        form_notation = form
    elif morph_type == "bound root":
        form_notation = "*" + form
    elif morph_type == "suffix":
        form_notation = "-" + form
    elif morph_type == "prefix":
        form_notation = form + "-"
    elif morph_type == "enclitic":
        form_notation = "=" + form
    elif morph_type == "proclitic":
        form_notation = form + "="
    else:
        raise Exception("unknown morph type: {}, in wordform: {}".format(morph_type, wordform))
    gloss = wordform.glosses[-1]
    return "{} ({})".format(form_notation, gloss)


def get_form_group_last_morpheme_form(wordform):
    assert type(wordform) is WordForm, wordform
    return wordform.morpheme_forms[-1]


def get_form_group_last_morpheme_gloss(wordform):
    assert type(wordform) is WordForm, wordform
    return wordform.glosses[-1]


def get_form_group_text_only(wordform):
    assert type(wordform) is WordForm, wordform
    return wordform.text

