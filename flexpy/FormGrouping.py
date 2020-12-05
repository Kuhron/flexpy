from flexpy.WordForm import WordForm, WordFormMorpheme


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
    return wordform.forms[-1]


def get_form_group_last_morpheme_gloss(wordform):
    assert type(wordform) is WordForm, wordform
    return wordform.glosses[-1]


def get_form_group_text_only(wordform):
    assert type(wordform) is WordForm, wordform
    return wordform.text

