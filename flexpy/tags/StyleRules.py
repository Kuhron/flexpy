from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class StyleRules:
    """A class for FLEx XML elements with the tag StyleRules

    :param el: the `xml.etree.ElementTree.Element object`
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, tag_dict):
        self.el = el
        self.tag_dict = tag_dict
        self.text = self.el.text
        self.fp = self.el.attrib.get("fp")

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def Prop(self):
        """Gets the child objects which have short tag of `Prop`, long tag of `Prop`"""
        return get_child_object(self.el, "Prop", self.tag_dict)
