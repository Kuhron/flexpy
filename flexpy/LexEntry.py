# replicating structure of <rt class="LexEntry">

from flexpy.FlexPyUtil import get_single_child



class LexEntry:
    def __init__(self, rt, rt_dict):
        self.rt = rt
        self.rt_dict = rt_dict
        self.populate_child_variables()

    def populate_child_variables(self):
        self.date_created = get_single_child(self.rt, "DateCreated").attrib["val"]
        self.date_modified = get_single_child(self.rt, "DateModified").attrib["val"]
        self.do_not_use_for_parsing = get_single_child(self.rt, "DoNotUseForParsing").attrib["val"]
        self.homograph_number = get_single_child(self.rt, "HomographNumber").attrib["val"]

        lexeme_form_el = get_single_child(self.rt, "LexemeForm")
        objsur = get_single_child(lexeme_form_el, "objsur")
        mo_stem_allomorph_el = self.rt_dict[objsur.attrib["guid"]]
        form_el = get_single_child(mo_stem_allomorph_el, "Form")
        # form_text = get_single_child(form_el, "AUni").text
        form_text_pieces = form_el.findall("AUni")
        form_text = ""
        for ftp in form_text_pieces:
            form_text += ftp.text
        self.lexeme_form = form_text

        self.parts_of_speech = []
        morpho_syntax_analyses_el = get_single_child(self.rt, "MorphoSyntaxAnalyses")
        if morpho_syntax_analyses_el is not None:
            objsurs = morpho_syntax_analyses_el.findall("objsur")
            for objsur in objsurs:
                mo_stem_msa_el = self.rt_dict[objsur.attrib["guid"]]
                part_of_speech_el = get_single_child(mo_stem_msa_el, "PartOfSpeech")
                if part_of_speech_el is not None:
                    objsur = get_single_child(part_of_speech_el, "objsur")
                    part_of_speech_rt = self.rt_dict[objsur.attrib["guid"]]
                    catalog_source_id = get_single_child(part_of_speech_rt, "CatalogSourceId")
                    if catalog_source_id is not None:
                        uni = get_single_child(catalog_source_id, "Uni")
                        self.parts_of_speech.append(uni.text)
        self.parts_of_speech = list(set(self.parts_of_speech))

        self.glosses = []
        senses_el = get_single_child(self.rt, "Senses")
        if senses_el is not None:
            objsurs = senses_el.findall("objsur")
            for objsur in objsurs:
                lex_sense_guid = objsur.attrib["guid"]
                lex_sense = self.rt_dict[lex_sense_guid]
                gloss_el = get_single_child(lex_sense, "Gloss")
                if gloss_el is None:
                    print("Warning: {} has no gloss".format(self))
                    continue
                auni = get_single_child(gloss_el, "AUni")
                gloss = auni.text
                self.glosses.append(gloss)

    def __repr__(self):
        return "<LexEntry \"{form}\" {pos} = {gloss}>".format(
            form=self.lexeme_form,
            pos=self.parts_of_speech,
            gloss=self.glosses,
        )
