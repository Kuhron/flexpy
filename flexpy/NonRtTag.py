import xml.etree.ElementTree as ET

from flexpy.TagDict import TagDict


class NonRtTag:
    """A FlexPy-specific class mean to hold information about XML elements with tags other than `rt`,
    which have various class names assigned by FLEx.
    """
    def __init__(self, el, parent_el, tag_dict):
        assert type(el) is ET.Element, "invalid element: {}".format(el)
        assert type(parent_el) is ET.Element, "invalid parent element: {}".format(parent_el)
        
        assert type(tag_dict) is TagDict
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict

    # def get_owner(self):
    #     # only construct this when asked, otherwise will take up too much memory
    #     return self.tag_dict.get_python_object_from_element(self.owner_el)

    def __repr__(self):
        return f"<tag={self.el.tag} parent={self.parent_el}>"

