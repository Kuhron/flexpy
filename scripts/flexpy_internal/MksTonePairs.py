from flexpy.Corpus import Corpus
from flexpy.tags.RtLexEntry import RtLexEntry
from flexpy.LexEntry import LexEntry
from flexpy.FlexPyUtil import get_tone_letters_from_string


project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
project_name = "IxpantepecMixtec"

corpus = Corpus(project_dir, project_name, include_punctuation=False)
tag_dict = corpus.tag_dict

# desired result:
# list of lexical items, each place it occurs in 1st position
# and each place it occurs in 2nd position
# show baseline tone pattern and perturbed tone pattern of both
# look at this big list to see what jumps out

by_lex_guid = {}

for text in corpus.texts:
    # print(f"current text is {text}")

    # iterate over MORPHEMES in the text (not across paragraph boundaries)
    # know the LexEntry that each of them belongs to
    if text.paragraphs is None:
        # print(f"skipping text {text} due to lack of paragraphs")
        continue
    for pg in text.paragraphs:
        # print("\n---- new paragraph ----\n")
        # print(f"current paragraph is: {pg}")
        # print(f"run texts is: {pg.run_texts}")
        # print(f"wordforms is: {pg.wordforms}")

        source = f"{text.name} {pg.paragraph_number}"

        morpheme_forms = []
        lex_entry_guids = []

        for wf in pg.wordforms:
            for morpheme in wf.get_morphemes():
                form = morpheme.form
                guid = morpheme.lex_entry_guid
                # some of the guids are None for unparsed stuff
                # don't pretend they're not there, but also don't put them in the dict
                if form in ["[H]", "[H?]", "[M]", "[M?]", "[L]", "[L?]"]:
                    # skip floating tone; DO pretend it's not there for sake of "next morpheme"
                    continue
                morpheme_forms.append(form)
                lex_entry_guids.append(guid)
        assert len(morpheme_forms) == len(lex_entry_guids)

        for form, guid in zip(morpheme_forms, lex_entry_guids):
            # print(guid, form)
            if guid is not None and guid not in by_lex_guid:
                by_lex_guid[guid] = {"first": {}, "second": {}}

        n_morphemes = len(morpheme_forms)
        for i in range(n_morphemes):
            is_first = i == 0
            is_last = i == n_morphemes - 1
            has_preceding = not is_first
            has_following = not is_last
            form = morpheme_forms[i]
            guid = lex_entry_guids[i]
            if guid is None:
                continue
            if has_following:
                # this morpheme is in first position
                following_form = morpheme_forms[i+1]
                following_guid = lex_entry_guids[i+1]
                if following_guid is not None:
                    if following_guid not in by_lex_guid[guid]["first"]:
                        by_lex_guid[guid]["first"][following_guid] = []
                    by_lex_guid[guid]["first"][following_guid].append([[form, following_form], source])
            if has_preceding:
                # this morpheme is in second position
                preceding_form = morpheme_forms[i-1]
                preceding_guid = lex_entry_guids[i-1]
                if preceding_guid is not None:
                    if preceding_guid not in by_lex_guid[guid]["second"]:
                        by_lex_guid[guid]["second"][preceding_guid] = []
                    by_lex_guid[guid]["second"][preceding_guid].append([[preceding_form, form], source])

form_strs_by_guid = {}
gloss_strs_by_guid = {}
for guid in by_lex_guid.keys():
    rt_lex_entry_el = tag_dict.get_single_element_by_guid(guid)
    lex_entry_obj = LexEntry(rt_lex_entry_el, tag_dict)
    forms = lex_entry_obj.allomorph_forms
    glosses = lex_entry_obj.glosses
    form_str = ", ".join(sorted(forms))
    gloss_str = ", ".join(sorted(glosses))
    form_strs_by_guid[guid] = form_str
    gloss_strs_by_guid[guid] = gloss_str

for guid, d in by_lex_guid.items():
    print(f"\n---- current guid: {guid}")
    forms = form_strs_by_guid[guid]
    glosses = gloss_strs_by_guid[guid]
    this_str = f"lex guid: {guid}\nglosses: {glosses}\nforms: {forms}\n"
    print(this_str)
    d_first = d["first"]
    d_second = d["second"]
    for sub_d in [d_first, d_second]:
        is_first = sub_d is d_first
        if is_first:
            print("when this lexeme comes first in a pair:\n")
        else:
            print("when this lexeme comes second in a pair:\n")
        for other_guid, forms_and_text_name in sub_d.items():
            other_forms = form_strs_by_guid[other_guid]
            other_glosses = gloss_strs_by_guid[other_guid]
            # this_ordinal = "first" if is_first else "second"
            other_ordinal = "second" if is_first else "first"
            other_str = f"{other_ordinal} word: lex guid: {other_guid}\nglosses: {other_glosses}\nforms: {other_forms}\n"
            print(other_str)
            for form_pair, source in forms_and_text_name:
                tone_patterns = [get_tone_letters_from_string(x) for x in form_pair]
                print(f"--> {form_pair}\t{tone_patterns}\t({source})")
                # TODO tone pattern change
            print()