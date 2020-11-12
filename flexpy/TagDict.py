from xml.etree import ElementTree as ET

from flexpy.FlexPyUtil import get_tag_class
import flexpy.XMLTagMap as xml_tag_map


class TagDict:
    def __init__(
            self, 
            by_tag=None, 
            by_tag_and_guid=None, 
            by_guid=None, 
            by_owner_guid=None,
            root=None,
            object_by_element=None,
    ):
        self.by_tag = by_tag if by_tag is not None else {}
        self.by_tag_and_guid = by_tag_and_guid if by_tag_and_guid is not None else {}
        self.by_guid = by_guid if by_guid is not None else {}
        self.by_owner_guid = by_owner_guid if by_owner_guid is not None else {}
        self.root = root if root is not None else None
        self.object_by_element = object_by_element if object_by_element is not None else {}
        self.dependency_dict = self.create_dependency_dict()

    @staticmethod
    def from_project_dir_and_name(project_dir, project_name):
        flex_dir = project_dir + "{}/".format(project_name)
        fp = flex_dir + "{}.fwdata".format(project_name)
        # print("getting TagDict from FLEx project {} at {}".format(project_name, fp))
        return TagDict.from_fwdata_file(fp)

    @staticmethod
    def from_fwdata_file(fp):
        tree = ET.parse(fp)
        root = tree.getroot()
        return TagDict.from_root(root)

    @staticmethod
    def from_root(root):
        # all elements in the XML
        # the dictionary is keyed by "class" attribute (e.g. "LexEntry") and then by FLEX's identifier for each object
        rts = list(root)
        children_tags = set(x.tag for x in rts)
        assert children_tags == {"rt"}, "unhandled tag types in element tree: {}, expected only \"rt\"".format(sorted(children_tags))

        all_elements = xml_tag_map.get_all_children_recursive(root)

        by_tag = {}
        by_tag_and_guid = {}
        by_guid = {}
        by_owner_guid = {}
        all_rt_attrib_keys = set()
        for el in all_elements:
            tag_key = xml_tag_map.get_tag_key_from_element(el, by_guid)
            if el.tag == "rt":
                all_rt_attrib_keys |= set(el.attrib.keys())
                guid = el.attrib["guid"]  # rts should all have a guid

                if tag_key not in by_tag:
                    by_tag[tag_key] = []
                by_tag[tag_key].append(el)

                if tag_key not in by_tag_and_guid:
                    by_tag_and_guid[tag_key] = {}
                assert guid not in by_tag_and_guid[tag_key], "guid {} already present for tag {} in TagDict".format(guid, tag_key)
                by_tag_and_guid[tag_key][guid] = el

                assert guid not in by_guid, "guid {} already present in TagDict".format(guid)
                by_guid[guid] = el

                try:
                    owner_guid = el.attrib["ownerguid"]  # only some have owners
                    if owner_guid not in by_owner_guid:
                        by_owner_guid[owner_guid] = []
                    by_owner_guid[owner_guid].append(el)
                except KeyError:
                    # has no owner
                    pass

            elif el.tag == "objsur":
                # only a surrogate for some rt element present elsewhere, ignore it
                # these only exist to show ownership/reference relationships
                pass

            else:
                # only rts should have guid and ownerguid
                assert "guid" not in el.attrib, "element has a guid but shouldn't: {}, guid={}".format(el, el.attrib["guid"])
                assert "ownerguid" not in el.attrib, "element has an ownerguid but shouldn't: {}, ownerguid={}".format(el, el.attrib["ownerguid"])

                if tag_key not in by_tag:
                    by_tag[tag_key] = []
                by_tag[tag_key].append(el)

        expected_all_rt_attrib_keys = {"class", "guid", "ownerguid"}
        assert all_rt_attrib_keys == expected_all_rt_attrib_keys, "rt elements have attributes {}, expected {}".format(all_rt_attrib_keys, expected_all_rt_attrib_keys)

        return TagDict(
            by_tag=by_tag,
            by_tag_and_guid=by_tag_and_guid,
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
                return self.by_tag_and_guid[index]
            except KeyError:
                pass  # don't want "another exception was raised while handling"

        # if got here, we had both KeyErrors occur
        # do actually want to raise in this case
        raise KeyError("key {} is neither a class name nor a guid".format(index))
    
    def get(self, index, backup_value=None):
        try:
            return self[index]
        except KeyError:
            return backup_value

    def keys(self):
        return self.by_guid.keys()

    def values(self):
        return self.by_guid.values()

    def items(self):
        return self.by_guid.items()

    def get_by_owner_guid(self, guid):
        return self.by_owner_guid.get(guid, [])

    def get_all_rts(self):
        return self.by_guid.values()

    def get_all_elements(self):
        elements = []
        for tag, lst in self.by_tag.items():
            elements += lst
        return elements

    def create_dependency_dict(self):
        return xml_tag_map.create_dependency_dict(self.root, self.by_guid)

    def print_dependency_dict(self):
        xml_tag_map.print_dependency_dict(self.root, self.by_guid)

    def get_python_object_from_element(self, el):
        assert type(el) is ET.Element, "invalid element: {}".format(el)
        if el.tag == "objsur":
            # resolve to the referent
            reference_guid = el.attrib["guid"]
            referent = self[reference_guid]
            assert referent.tag != "objsur", "objsur {} refers to another objsur {}".format(el, referent)
            return self.get_python_object_from_element(referent)
        try:
            # fetch already-created object
            return self.object_by_element[el]
        except KeyError:
            # create new object
            # print("creating new python object for {}".format(el))
            class_object = get_tag_class(el)
            # initialize it
            return class_object(el, tag_dict=self)

    def fill_out_objects(self):
        # this will try to do all of them, and can encounter recursion errors
        for el in self.get_all_elements():
            python_object = self.get_python_object_from_element(el)
            self.object_by_element[el] = python_object
            print("successfully filled out object for element {}".format(el))
        print("done filling out elements")