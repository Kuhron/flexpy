class AffixSelector:
    def __init__(self, form_str, gloss_regex):
        print("Warning: AffixSelector class is specific to Bongu language at the moment")
        self.form_str = form_str
        self.gloss_regex = gloss_regex

    def has_person_feature(self): 
        return any(x in self.gloss_regex for x in ["1", "2", "3"])

    def is_syncretic_for_person(self):
        return any(x in self.gloss_regex for x in ["12", "23"]) or not self.has_person_feature()

    def is_syncretic_for_number(self):
        return "ns" in self.gloss or not self.has_person_feature()  # e.g. irr.ss has no person or number feature, is syncretic to the max
    
    def is_syncretic(self):
        return self.is_syncretic_for_person() or self.is_syncretic_for_number()
