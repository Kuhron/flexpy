from flexpy.AffixSelector import AffixSelector


bongu_agreement_affixes = [
    AffixSelector("aim", r"2s\.fpst"),
    AffixSelector("ain", r"3s\.fpst"),
    AffixSelector("am", r"2s\.ifut"),
    AffixSelector("an", r"3s\.ifut"),
    # AffixSelector("aq", r"irr.*"),  # could agree with anything, so can't distinguish agree from disagree
    AffixSelector("balan", r"23ns.*"),
    AffixSelector("ban", r"23ns.*"),
    AffixSelector("beb", r"23ns.*"),
    AffixSelector("beben", r"23ns.*"),
    AffixSelector("ber", r"23ns.*"),
    AffixSelector("beren", r"23ns.*"),
    AffixSelector("berlan", r"23d.*"),
    AffixSelector("bes", r"23ns.*"),
    AffixSelector("besen", r"23ns.*"),
    AffixSelector("beslan", r"23d.*"),
    AffixSelector("buleren", r"23d.*"),
    # "-bun" is not well understood
    AffixSelector("bus", r"3ns.*"),
    AffixSelector("busen", r"3ns.*"),
    AffixSelector("busun", r"3ns.*"),
    AffixSelector("e", r"2s\.imp"),
    AffixSelector("eben", r"23ns.*"),
    AffixSelector("eblan", r"23d.*"),
    AffixSelector("em", r"2s.*"),
    AffixSelector("emen", r"1s\.fpst"),  # don't use character class like r"[12]" because then it will think it's syncretic for person (has substr "12")
    AffixSelector("emen", r"2s\.fut\?"),  # just treat this as a separate suffix from -emen 1s.fpst
    AffixSelector("emun", r"1ns.*"),
    AffixSelector("en", r"3s.*"),
    AffixSelector("eqen", r"3s\.prs\?"),
    AffixSelector("eren", r"3s.*"),
    AffixSelector("es", r"3s\.r\.ss"),  # this one is not syncretic
    # AffixSelector("es", r"irr.*"),  # this one IS syncretic, for all person and numbers  # can't distinguish agreeing from disagreeing pronouns
    AffixSelector("esen", r"3s.*"),
    # -esen as different-subject marker is not well understood
    AffixSelector("ib", r"2ns\.imp"),
    # -im not understood
    AffixSelector("man", r"1s.*"),
    AffixSelector("mem", r"1s.*"),
    AffixSelector("memen", r"1s.*"),
    AffixSelector("memes", r"12s.*"),
    AffixSelector("meq", r"2s.*"),
    AffixSelector("meqen", r"2s.*"),
    AffixSelector("mere", r"2s.*"),
    AffixSelector("meren", r"12s.*"),
    AffixSelector("mes", r"12s.*"),
    AffixSelector("mesen", r"12s.*"),
    AffixSelector("mulan", r"1d\.rpst"),
    AffixSelector("mum", r"1ns.*"),
    AffixSelector("mun", r"1ns.*"),
    AffixSelector("mur", r"1ns.*"),
    AffixSelector("muren", r"1ns.*"),
    AffixSelector("mus", r"1ns.*"),
    AffixSelector("musen", r"1ns.*"),
]