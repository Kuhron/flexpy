from xml.etree import ElementTree as ET

from flexpy.Text import Text
import flexpy.XMLTagMap as xml_tag_map


class RtDict:
    def __init__(
            self, 
            by_class_and_guid=None, 
            by_guid=None, 
            by_owner_guid=None,
            root=None,
    ):
        self.by_class_and_guid = by_class_and_guid if by_class_and_guid is not None else {}
        self.by_guid = by_guid if by_guid is not None else {}
        self.by_owner_guid = by_owner_guid if by_owner_guid is not None else {}
        self.root = root if root is not None else None

    @staticmethod
    def from_fwdata_file(fp):
        tree = ET.parse(fp)
        root = tree.getroot()
        return RtDict.from_root(root)

    @staticmethod
    def from_root(root):
        # all <rt> elements in the XML
        # the dictionary is keyed by "class" attribute (e.g. "LexEntry") and then by FLEX's identifier for each object
        all_children = list(root)
        children_tags = set(x.tag for x in all_children)
        assert children_tags == {"rt"}, "unhandled tag types in element tree: {}, expected only \"rt\"".format(sorted(children_tags))
        rts = all_children
        # rts = root.findall("rt")

        by_class_and_guid = {}
        by_guid = {}
        by_owner_guid = {}
        all_rt_attrib_keys = set()
        # all_rt_classes = set()
        for rt in rts:
            all_rt_attrib_keys |= set(rt.attrib.keys())
            class_name = rt.attrib["class"]  # rts should all have a class
            # all_rt_classes.add(class_name)
            if class_name not in by_class_and_guid:
                by_class_and_guid[class_name] = {}
            guid = rt.attrib["guid"]  # rts should all have a guid
            by_class_and_guid[class_name][guid] = rt
            by_guid[guid] = rt

            try:
                owner_guid = rt.attrib["ownerguid"]  # only some have owners
                if owner_guid not in by_owner_guid:
                    by_owner_guid[owner_guid] = []
                by_owner_guid[owner_guid].append(rt)
            except KeyError:
                # has no owner
                pass

            # tried moving this to XMLTagMap.py
            # rt_children = list(rt)
            # rt_children_tags = set(x.tag for x in rt_children)
            # tag_child_dict_key = "rt.{}".format(class_name)
            # if tag_child_dict_key not in tag_child_dict:
            #     tag_child_dict[tag_child_dict_key] = set()
            # tag_child_dict[tag_child_dict_key] |= rt_children_tags

        expected_all_rt_attrib_keys = {"class", "guid", "ownerguid"}
        assert all_rt_attrib_keys == expected_all_rt_attrib_keys, "rt elements have attributes {}, expected {}".format(all_rt_attrib_keys, expected_all_rt_attrib_keys)
        # print("all rt classes: {}".format(sorted(all_rt_classes)))

        return RtDict(
            by_class_and_guid=by_class_and_guid,
            by_guid=by_guid,
            by_owner_guid=by_owner_guid,
            root=root,  # store for later use e.g. printing dependencies of elements
        )

    def __getitem__(self, index):
        try:
            return self.by_guid[index]
        except KeyError:
            try:
                # try giving the class-specific dict
                return self.by_class_and_guid[index]
            except KeyError:
                print("Warning: key {} is neither a class name nor a guid".format(index))
                return None

    def get_by_owner_guid(self, guid):
        return self.by_owner_guid.get(guid, [])

    def get_texts(self):
        text_elements = self["Text"]
        texts = []
        for guid, rt in text_elements.items():
            text = Text(guid, rt, self)
            texts.append(text)
        # print("there are {} texts with contents".format(sum(x.has_contents() for x in texts)))
        return texts

    def print_dependency_dict(self):
        xml_tag_map.print_dependency_dict(self.root, self.by_guid)

