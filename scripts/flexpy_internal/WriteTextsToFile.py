import os
from flexpy.Corpus import Corpus
from flexpy.LexEntry import LexEntry
from flexpy.PunctuationForm import PunctuationForm

lg_name = "Horokoi"
project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
fwdata_fp = os.path.join(project_dir, lg_name, f"{lg_name}.fwdata")
corpus = Corpus(fwdata_fp, include_punctuation=True)

output_dir = f"/home/wesley/{lg_name}/TextDump"
# corpus.write_texts_to_file(output_dir)

# want to be able to print all of the lines in Analyze view: Word, Morphemes, LexEntries, LexGloss, LexGramInfo, WordGloss, WordCat
# and user can decide what of these they want and how they want to pre-process before printing
# (e.g. I want cases where a word is unanalyzed to treat that wordform as one morpheme with a blank gloss, so it will show up nicely in my text files for parsing outside of FLEx)

# do it more myself here with the atoms that already exist, don't keep making custom ways of printing stuff using the Corpus object
morpheme_delimiter = "-"  # don't bother with marking clitics differently here
word_delimiter = "\t"
for text in corpus.texts:
    # print(f"{text = }")
    # print(len(text.paragraphs), "paragraphs")
    # print()
    output_fname = f"{text.abbreviation}.txt"
    output_fp = os.path.join(output_dir, output_fname)
    lines_to_write = []
    for paragraph_i, paragraph in enumerate(text.paragraphs):
        paragraph_number = paragraph_i + 1
        print(f"{text.abbreviation} {paragraph_number}")  # for finding where errors occur in the database
        # print(f"{paragraph = }")
        # print(len(paragraph.wordforms), "wordforms")
        # print()
        word_str_items = []
        morpheme_str_items = []
        lex_entry_str_items = []
        lex_gloss_str_items = []
        lex_gram_info_str_items = []
        for wordform in paragraph.wordforms:
            # print(f"{wordform = }")

            word = wordform.baseline
            # print(f"{word = }")
            word_str_items.append(word)

            if type(wordform) is PunctuationForm:
                morphemes = []
            else:
                morphemes = wordform.morpheme_forms
            morphemes = [x.replace(morpheme_delimiter, "\\"+morpheme_delimiter) for x in morphemes]
            morpheme_str_items.append(morpheme_delimiter.join(morphemes))

            if type(wordform) is PunctuationForm:
                lex_entry_guids = []
                lex_entry_forms = []
            else:
                lex_entry_guids = wordform.lex_entry_guids
                # print(f"{lex_entry_guids = }")
                lex_entry_forms = []
                for g in lex_entry_guids:
                    if g is None:
                        lex_entry_forms.append("?")
                    else:
                        rt, = corpus.tag_dict[g]
                        lex_entry = LexEntry(rt, corpus.tag_dict)
                        # print("le", lex_entry)
                        lex_entry_forms.append(lex_entry.lexeme_form)
                        # print("gl", lex_entry.glosses)
            # print("fm", lex_entry_forms)
            lex_entry_str_items.append(morpheme_delimiter.join(lex_entry_forms))

            if type(wordform) is PunctuationForm:
                lex_gloss = []
            else:
                lex_gloss = wordform.glosses
            lex_gloss_str_items.append(morpheme_delimiter.join("?" if x is None else x for x in lex_gloss))

            if type(wordform) is PunctuationForm:
                lex_gram_info = []
            else:
                lex_gram_info = wordform.poses
            lex_gram_info_str_items.append(morpheme_delimiter.join("?" if x is None else x for x in lex_gram_info))

            # I don't care about these right now
            # word_gloss = ?
            # print(word_gloss)
            # word_cat = ?
            # print(word_cat)

        free_translation_str = paragraph.get_free_translation()
        free_translation_str = "" if free_translation_str is None else free_translation_str

        paragraph_lines = [
            f"Location: {text.abbreviation} {paragraph_number}", 
            "Word:" + word_delimiter + word_delimiter.join(word_str_items),
            "Morphemes:" + word_delimiter + word_delimiter.join(morpheme_str_items),
            "LexEntries:" + word_delimiter + word_delimiter.join(lex_entry_str_items),
            "LexGloss:" + word_delimiter + word_delimiter.join(lex_gloss_str_items),
            "LexGramInfo:" + word_delimiter + word_delimiter.join(lex_gram_info_str_items),
            "Free:" + word_delimiter + free_translation_str,
        ]
        lines_to_write += paragraph_lines + [""]
    with open(output_fp, "w") as f:
        for l in lines_to_write:
            f.write(l + "\n")
    print(f"written to {output_fp}")
