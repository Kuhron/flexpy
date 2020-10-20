from xml.etree import ElementTree as ET


class RtDict:
    def __init__(
            self, 
            by_class_and_guid=None, 
            by_guid=None, 
            by_owner_guid=None,
    ):
        self.by_class_and_guid = by_class_and_guid if by_class_and_guid is not None else {}
        self.by_guid = by_guid if by_guid is not None else {}
        self.by_owner_guid = by_owner_guid if by_owner_guid is not None else {}

    @staticmethod
    def from_fwdata_file(fp):
        tree = ET.parse(fp)
        root = tree.getroot()
        return RtDict.from_root(root)

    @staticmethod
    def from_root(root):
        # all <rt> elements in the XML
        # the dictionary is keyed by "class" attribute (e.g. "LexEntry") and then by FLEX's identifier for each object
        rts = root.findall("rt")
        by_class_and_guid = {}
        by_guid = {}
        by_owner_guid = {}
        for rt in rts:
            class_name = rt.attrib["class"]
            if class_name not in by_class_and_guid:
                by_class_and_guid[class_name] = {}
            guid = rt.attrib["guid"]
            by_class_and_guid[class_name][guid] = rt
            by_guid[guid] = rt

            try:
                owner_guid = rt.attrib["ownerguid"]
                if owner_guid not in by_owner_guid:
                    by_owner_guid[owner_guid] = []
                by_owner_guid[owner_guid].append(rt)
                # print("{} is owned by {}".format(guid, owner_guid))
            except KeyError:
                # has no owner
                pass

        return RtDict(
            by_class_and_guid=by_class_and_guid,
            by_guid=by_guid,
            by_owner_guid=by_owner_guid,
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

    def get_by_owner_guid(self, index):
        return self.by_owner_guid.get(index, [])


