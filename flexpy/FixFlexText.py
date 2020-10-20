import sys

fp = sys.argv[1]

print("fixing {}".format(fp))

with open(fp) as f:
    contents = f.read()

to_lang = "dnw"
from_lang_str = "lang=\"en\""
to_lang_str = "lang=\"{}\"".format(to_lang)
txt_prefix = "type=\"txt\" "
language_prefix = "<language "

for prefix in [txt_prefix, language_prefix]:
    contents = contents.replace(prefix+from_lang_str, prefix+to_lang_str)

import xml.etree.ElementTree as ET
root = ET.fromstring(contents)

# find blank annotations to remove them
doc = root
inter = doc.find("interlinear-text")
pgs_elem = inter.find("paragraphs")
pgs = pgs_elem.findall("paragraph")
elems_to_remove = []
for paragraph in pgs:
    items = paragraph.iter("item")
    delete = False
    segnum = None
    for item in items:
        typ = item.get("type")
        if typ in ["txt", "gls"]:
            if item.text is None or item.text == "...":
                delete = True
            else:
                pass #print("not deleting item.text={}".format(item.text))
                #print(item)
        elif typ == "segnum":
            segnum = item.text
        else:
            print("unknown item type {}".format(typ))
    if delete:
        print("removing segnum {}".format(segnum))
        elems_to_remove.append(paragraph)

for el in elems_to_remove:
    pgs_elem.remove(el)



output_fp = "FixFlexTextOutput.flextext"
#tree = ET.ElementTree(root)
s = ET.tostring(root, encoding='utf8', method='xml')
#tree.write(output_fp)
with open(output_fp, "wb") as f:
    f.write(s)

