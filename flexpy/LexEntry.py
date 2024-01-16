# replicating structure of <rt class="LexEntry">

import xml.etree.ElementTree as ET

from flexpy.FlexPyUtil import (get_single_child, get_children, 
    get_unique_strs_from_form_as_list, elstr)
from flexpy.tags.Form import Form
from flexpy.tags.RtLexEntry import RtLexEntry
from flexpy.tags.RtLexEntryRef import RtLexEntryRef


class LexEntry:
    """A FlexPy-specific class (i.e., not from FLEx's XML structure)
    intended to make it easier to work with lexeme entries

    :param rt: the XML element with this lexeme entry's information
    :type rt: xml.etree.ElementTree.Element
    :param tag_dict:
    :type tag_dict: TagDict
    """
    def __init__(self, rt, tag_dict):
        assert type(rt) is ET.Element, rt
        self.rt = rt
        self.tag_dict = tag_dict

        # child variables placeholders
        self.date_created = None
        self.date_modified = None
        self.do_not_use_for_parsing = None
        self.homograph_number = None
        self.lexeme_form = None
        self.allomorph_forms = []
        self.parts_of_speech = []
        self.glosses = []

        self.is_variant = None
        self.parent_lexeme_guid = None

        self.populate_child_variables()

    def populate_child_variables(self):
        lex_entry_obj = RtLexEntry(self.rt, tag_dict=self.tag_dict)
        
        self.date_created = get_single_child(self.rt, "DateCreated").attrib["val"]
        self.date_modified = get_single_child(self.rt, "DateModified").attrib["val"]
        self.do_not_use_for_parsing = get_single_child(self.rt, "DoNotUseForParsing").attrib["val"]
        self.homograph_number = get_single_child(self.rt, "HomographNumber").attrib["val"]

        # lexeme form and allomorphs
        lexeme_form_el = get_single_child(self.rt, "LexemeForm")
        objsur = get_single_child(lexeme_form_el, "objsur")
        mo_stem_allomorph_el = self.tag_dict.get_single_element_by_guid(objsur.attrib["guid"])
        allomorph_forms = self.get_forms_from_mo_stem_allomorph_el(mo_stem_allomorph_el)
        if allomorph_forms is not None:
            self.lexeme_form = allomorph_forms[0]
            self.allomorph_forms += allomorph_forms

        alternate_forms_el = get_single_child(self.rt, "AlternateForms")
        if alternate_forms_el is not None:
            objsurs = get_children(alternate_forms_el, "objsur")
            for objsur in objsurs:
                mo_stem_allomorph_el = self.tag_dict.get_single_element_by_guid(objsur.attrib["guid"])
                allomorph_forms = self.get_forms_from_mo_stem_allomorph_el(mo_stem_allomorph_el)
                if allomorph_forms is not None:
                    self.allomorph_forms += allomorph_forms

        # parts of speech
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

        # glosses
        senses_el = get_single_child(self.rt, "Senses")
        if senses_el is not None:
            objsurs = senses_el.findall("objsur")
            for objsur in objsurs:
                lex_sense_guid = objsur.attrib["guid"]
                lex_sense_rt = self.tag_dict.get_single_element_by_guid(lex_sense_guid)
                gloss_el = get_single_child(lex_sense_rt, "Gloss")
                if gloss_el is None:
                    continue
                auni = get_single_child(gloss_el, "AUni")
                gloss = auni.text
                self.glosses.append(gloss)
        
        # figure out if it's a variant of another LexEntry
        # if it is, it will have tag for LexEntryRef, whose ComponentLexemes points to the parent

        # # this stuff is without using flexpy.tags:
        # entry_refs_el = get_single_child(self.rt, "EntryRefs")
        # self.is_variant = entry_refs_el is not None
        # if self.is_variant:
        #     objsurs = entry_refs_el.findall("objsur")
        #     for objsur in objsurs:
        #         lex_entry_ref_guid = objsur.attrib["guid"]
        #         lex_entry_ref_rt = self.tag_dict.get_single_element_by_guid(lex_entry_ref_guid)
        #         lex_entry_ref_obj = RtLexEntryRef(lex_entry_ref_rt)
        #         component_lexemes_el = lex_entry_ref_rt.ComponentLexemes()
        #         print(self)
        #         print(component_lexemes_el)
        #         input("check")

        # this is equivalent using flexpy.tags objects for ease of reading/writing
        # essentially flexpy.tags is an API within the flexpy API
        entry_refs = lex_entry_obj.EntryRefs()
        # print(f"for lex entry {self} got entry_refs {entry_refs}")
        # self.is_variant = entry_refs is not None  # not true, compounds can also have this
        if entry_refs is None:
            self.is_variant = False
        else:
            self.is_variant = False  # unless proven otherwise in the ensuing search for VariantEntryTypes tag
            parent_lexeme_rts = []
            rt_lex_entry_ref = entry_refs.RtLexEntryRef()
            for rt_lex_entry_ref_obj in rt_lex_entry_ref:
                has_variant_entry_types = rt_lex_entry_ref_obj.VariantEntryTypes() is not None
                if has_variant_entry_types:
                    self.is_variant = True
                else:
                    continue  # not a variant
                component_lexemes = rt_lex_entry_ref_obj.ComponentLexemes()
                # print(f"component lexemes is: {component_lexemes}")

                # the lexeme can be a variant of a lex entry or of a specific sense
                # if it's a lex entry variant then great
                rt_lex_entry = component_lexemes.RtLexEntry()
                # print(f"rt lex entry is: {rt_lex_entry}")
                for rt_lex_entry_obj in rt_lex_entry:
                    parent_lexeme_rts.append(rt_lex_entry_obj.el)
                
                # if it's a sense variant, then the parent lexeme needs to be gotten from that
                rt_lex_sense = component_lexemes.RtLexSense()
                # print(f"rt lex sense is: {rt_lex_sense}")
                for rt_lex_sense_obj in rt_lex_sense:
                    parent_lexeme_rt = rt_lex_sense_obj.owner_el
                    # not obj.parent_el, since that will just be the ComponentLexemes tag that led here
                    parent_lexeme_rts.append(parent_lexeme_rt)

            if len(parent_lexeme_rts) > 1:
                # for sake of printing the objects for me to go fix them in FLEx,
                # make some temporary LexEntry objects (this same class)
                parent_lexeme_strs = []
                for parent_lexeme_rt in parent_lexeme_rts:
                    temp_lex_entry = LexEntry(parent_lexeme_rt, self.tag_dict)
                    parent_lexeme_strs.append(repr(temp_lex_entry))
                print("Error: got multiple parent lexemes")
                print("current lexeme:", self)
                for parent_lexeme_str in parent_lexeme_strs:
                    print("parent lexeme:", parent_lexeme_str)
                raise ValueError("multiple parent lexemes")
            elif self.is_variant:
                parent_lexeme_rt = parent_lexeme_rts[0]
                # print(f"parent lexeme rt is {elstr(parent_lexeme_rt)}")
                self.parent_lexeme_guid = parent_lexeme_rt.attrib["guid"]
            else:
                self.parent_lexeme_guid = None  # it should already be None, but just for reader
        
        assert self.is_variant is not None  # don't want to leave it with falsey value of None

        # after processing all of this, NOW you do the warning about bad words
        if self.lexeme_form is None:
            print(f"Warning: {self} has no form")
        if not self.is_variant and len(self.glosses) == 0:
            # if it's a variant, get this and other info from the parent lexeme
            print(f"Warning: {self} has no gloss")

    def get_forms_from_mo_stem_allomorph_el(self, mo_stem_allomorph_el):
        form_el = get_single_child(mo_stem_allomorph_el, "Form")
        if form_el is None:
            return []

        form_obj = Form(form_el, tag_dict=self.tag_dict, parent_el=mo_stem_allomorph_el)
        forms = get_unique_strs_from_form_as_list(form_obj)
        # if len(forms) == 1:
        #     return forms[0]
        # else:
        #     return forms
        return forms  # bad idea to return multiple types based only on number of items!

    def __repr__(self):
        if self.is_variant:
            parent_lex_entry_el = self.tag_dict.get_single_element_by_guid(self.parent_lexeme_guid)
            parent_lex_entry_obj = LexEntry(parent_lex_entry_el, self.tag_dict) if parent_lex_entry_el is not None else None
            parent_str = repr(parent_lex_entry_obj) if parent_lex_entry_obj is not None else "None (perhaps uninitialized due to error)"
            variant_str = f"(variant of {parent_str})"
            s = f"<LexEntry \"{self.lexeme_form}\" {variant_str}>"
        else:
            s = f"<LexEntry \"{self.lexeme_form}\" {self.parts_of_speech} = {self.glosses}>"
        
        return s

    def tsv_repr(self):
        forms = self.allomorph_forms
        assert type(forms) is list
        print("forms = {}".format(forms))
        for form in forms:
            assert "\t" not in form and "\n" not in form, repr(form)
        form_str = ",".join(forms)
        pos_str = ",".join(str(x) for x in self.parts_of_speech)
        assert "\t" not in pos_str and "\n" not in pos_str
        gloss_str = ",".join(str(x) for x in self.glosses)
        assert "\t" not in gloss_str and "\n" not in gloss_str
        return "{}\t{}\t{}".format(form_str,pos_str,gloss_str)
