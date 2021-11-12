# replicating structure of <rt class="LexEntry">

import xml.etree.ElementTree as ET

from flexpy.FlexPyUtil import get_single_child, get_unique_strs_from_form_as_list
from flexpy.tags.Form import Form


class LexEntry:
    """A FlexPy-specific class (i.e., not from FLEx's XML structure)
    intended to make it easier to work with lexeme entries

    :param rt: the XML element with this lexeme entry's information
    :type rt: xml.etree.ElementTree.Element
    :param tag_dict:
    :type tag_dict: TagDict
    """
    def __init__(self, rt, tag_dict):
        assert type(rt) is ET.Element, self.rt
        self.rt = rt
        self.tag_dict = tag_dict
        self.populate_child_variables()

    def populate_child_variables(self):
        self.date_created = get_single_child(self.rt, "DateCreated").attrib["val"]
        self.date_modified = get_single_child(self.rt, "DateModified").attrib["val"]
        self.do_not_use_for_parsing = get_single_child(self.rt, "DoNotUseForParsing").attrib["val"]
        self.homograph_number = get_single_child(self.rt, "HomographNumber").attrib["val"]

        lexeme_form_el = get_single_child(self.rt, "LexemeForm")
        objsur = get_single_child(lexeme_form_el, "objsur")
        mo_stem_allomorph_el = self.tag_dict.get_single_element_by_guid(objsur.attrib["guid"])
        form_el = get_single_child(mo_stem_allomorph_el, "Form")
        if form_el is not None:
            form_obj = Form(form_el, self.tag_dict)
            forms = get_unique_strs_from_form_as_list(form_obj)
            if len(forms) == 1:
                self.lexeme_form = forms[0]
            else:
                self.lexeme_form = forms
        else:
            self.lexeme_form = None

        self.parts_of_speech = []
        morpho_syntax_analyses_el = get_single_child(self.rt, "MorphoSyntaxAnalyses")
        if morpho_syntax_analyses_el is not None:
            objsurs = morpho_syntax_analyses_el.findall("objsur")
            for objsur in objsurs:
                mo_stem_msa_el = self.tag_dict.get_single_element_by_guid(objsur.attrib["guid"])
                part_of_speech_el = get_single_child(mo_stem_msa_el, "PartOfSpeech")
                if part_of_speech_el is not None:
                    objsur = get_single_child(part_of_speech_el, "objsur")
                    part_of_speech_rt = self.tag_dict.get_single_element_by_guid(objsur.attrib["guid"])
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
                lex_sense = self.tag_dict.get_single_element_by_guid(lex_sense_guid)
                gloss_el = get_single_child(lex_sense, "Gloss")
                if gloss_el is None:
                    continue
                auni = get_single_child(gloss_el, "AUni")
                gloss = auni.text
                self.glosses.append(gloss)

        # after processing all of this, NOW you do the warning about bad words
        if self.lexeme_form is None:
            print(f"Warning: {self} has no gloss")
        if len(self.glosses) == 0:
            print(f"Warning: {self} has no gloss")

    def __repr__(self):
        return "<LexEntry \"{form}\" {pos} = {gloss}>".format(
            form=self.lexeme_form,
            pos=self.parts_of_speech,
            gloss=self.glosses,
        )

    def tsv_repr(self):
        form = self.lexeme_form
        if type(form) is str:
            forms = [form]
            if "awna" in form:
                raise Exception(form)
        else:
            assert type(form) is list
            forms = form
            print("forms = {}".format(forms))
        for form in forms:
            assert "\t" not in form and "\n" not in form, repr(form)
        form = ",".join(forms)
        pos = ",".join(str(x) for x in self.parts_of_speech)
        assert "\t" not in pos and "\n" not in pos
        gloss = ",".join(str(x) for x in self.glosses)
        assert "\t" not in gloss and "\n" not in gloss
        return "{}\t{}\t{}".format(form,pos,gloss)
