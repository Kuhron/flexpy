from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class PromptText:
    """A class for FLEx XML elements with the tag PromptText

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

    def Uni(self):
        """Gets the child objects which have short tag of `Uni`, long tag of `Uni`"""
        return get_child_object(self.el, "Uni", self.tag_dict)
