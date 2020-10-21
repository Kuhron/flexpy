from xml.etree import ElementTree as ET
import random

# FlexPy-specific classes
from flexpy.FlexPyUtil import get_single_child
from flexpy.RtDict import RtDict
from flexpy.Text import Text


    # in vim, type gg=G in normal mode (no colon) to indent xml file
    # this works because I added the following in ~/.vimrc
    # :set equalprg=xmllint\ --format\ -
    # and can type ':set nowrap' (no quotes) to stop wrapping the long lines of semantic domain descriptions
    # easier to see the .fwdata structure this way
 
    # tree = ET.parse(fp)
    # root = tree.getroot()


def get_frequencies_naive(strs):
    assert type(strs) is list
    d = {}
    chars_to_delete = ".,/?!;\'\""
    for s in strs:
        for c in chars_to_delete:
            s = s.replace(c, "")
        words = s.lower().strip().split()
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
    return d


def report_frequencies_naive(strs):
    d = get_frequencies_naive(strs)
    tups = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    top_n = 50
    total_words = sum(d.values())
    print("---- report of top {} most frequent words (naive) out of {} words total ----".format(top_n, total_words))
    for tup in tups[:top_n]:
        print("Word {0} occurs {1} times".format(*tup))




