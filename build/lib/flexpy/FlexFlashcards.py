raise Exception("this is broken")

def run_flashcards(project_name, rt_dict):
    raise Exception ("FIXME")
    # asks user random lexicon entries as a vocabulary quiz
    lex_entries = rt_dict["LexEntry"]
    for lex in lex_entries.values():
        lexeme_form = get_single_child(lex, "LexemeForm")
        objsur = get_single_child(lexeme_form, "objsur")
        lexeme_form_guid = objsur.attrib["guid"]
        senses_elements = lex.findall("Senses")
        if len(senses_elements) == 0:
            continue
        
        sense_texts = []
        for sense_element in senses_elements:
            sense_objsurs = sense_element.findall("objsur")  # not necessarily only one
            for sense_objsur in sense_objsurs:
                sense_guid = objsur.attrib["guid"]
                form_classes = ["MoStemAllomorph", "MoAffixAllomorph", "WfiWordform"]
                form_found = False
                for fcl in form_classes:
                    try:
                        lexeme_form_rt = rt_dict["MoStemAllomorph"][lexeme_form_guid]
                        form = get_single_child(lexeme_form_rt, "Form")
                        auni = get_single_child(form, "AUni")
                        lexeme_form = auni.text
                        form_found = True
                    except KeyError:
                        continue
            
                if not form_found:
                    print("form not found with guid {}".format(lexeme_form_guid))
                    input("press enter to move on to next rt tag")
                    continue
            
                sense_rt = rt_dict["LexSense"][sense_guid]
                gloss = get_single_child(sense_rt, "Gloss")
                auni = get_single_child(gloss, "AUni")
                sense_text = auni.text
                sense_texts.append(sense_text)

        sense = "; ".join(sense_texts)
    
        print("\n--- new item ---")
        lang_first = random.random() < 0.7
        if lang_first:
            print("{}: {}".format(project_name, lexeme_form))
            input("English?: ")
            print("answer: {}".format(sense))
        else:
            print("English: {}".format(sense))
            input("{}?: ".format(project_name))
            print("answer: {}".format(lexeme_form))
        input("press enter to continue")
        # print(lexeme_form, sense)
        # input("press2")


