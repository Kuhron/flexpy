TONE_CHAR_TO_TONE_LETTER = {
    "\u0300": "L",
    "\u0304": "M",
    "\u0301": "H",
    "\u1dc5": "LM",
    "\u030c": "LH",
    "\u1dc6": "ML",
    "\u1dc4": "MH",
    "\u1dc7": "HM",
    "\u0302": "HL",
}

# http://pinyin.info/unicode/diacritics.html
COMBINED_CHARS = {
    "\u00e0": ["a", "L"],
    "\u0101": ["a", "M"],
    "\u00e1": ["a", "H"],
    "\u01ce": ["a", "LH"],
    "\u00e2": ["a", "HL"],
    "\u00e8": ["e", "L"],
    "\u0113": ["e", "M"],
    "\u00e9": ["e", "H"],
    "\u011b": ["e", "LH"],
    "\u00ea": ["e", "HL"],
    "\u00ec": ["i", "L"],
    "\u012b": ["i", "M"],
    "\u00ed": ["i", "H"],
    "\u01d0": ["i", "LH"],
    "\u00ee": ["i", "HL"],
    "\u00f2": ["o", "L"],
    "\u014d": ["o", "M"],
    "\u00f3": ["o", "H"],
    "\u01d2": ["o", "LH"],
    "\u00f4": ["o", "HL"],
    "\u00f9": ["u", "L"],
    "\u016b": ["u", "M"],
    "\u00fa": ["u", "H"],
    "\u01d4": ["u", "LH"],
    "\u00fb": ["u", "HL"],
}

COMBINED_CHAR_TO_SEGMENT_ONLY = {k: v[0] for k, v in COMBINED_CHARS.items()}
COMBINED_CHAR_TO_TONE_LETTER = {k: v[1] for k, v in COMBINED_CHARS.items()}

