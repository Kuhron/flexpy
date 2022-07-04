from flexpy.Rt import Rt
from flexpy.FlexPyUtil import get_child_object, get_ordered_child_objects

class RtStStyle(Rt):
    """A class for FLEx XML elements with the tag rt

    :param el: the `xml.etree.ElementTree.Element` object
    :param tag_dict: the `TagDict` object organizing the Elements in the FLEx project
    """
    def __init__(self, el, parent_el=None, tag_dict=None):
        super().__init__(el, parent_el=parent_el, tag_dict=tag_dict)
        self.el = el
        self.parent_el = parent_el
        self.tag_dict = tag_dict
        self.text = self.el.text

    def get_ordered_child_objects(self):
        """Gets the child objects of this element, in their order of appearance in the FLEx XML"""
        return get_ordered_child_objects(self.el, self.tag_dict)

    def BasedOn(self):
        """Gets the child objects which have short tag of `BasedOn`, long tag of `BasedOn`"""
        return get_child_object(self.el, "BasedOn", self.tag_dict)

    def Context(self):
        """Gets the child objects which have short tag of `Context`, long tag of `Context`"""
        return get_child_object(self.el, "Context", self.tag_dict)

    def Function(self):
        """Gets the child objects which have short tag of `Function`, long tag of `Function`"""
        return get_child_object(self.el, "Function", self.tag_dict)

    def IsBuiltIn(self):
        """Gets the child objects which have short tag of `IsBuiltIn`, long tag of `IsBuiltIn`"""
        return get_child_object(self.el, "IsBuiltIn", self.tag_dict)

    def IsModified(self):
        """Gets the child objects which have short tag of `IsModified`, long tag of `IsModified`"""
        return get_child_object(self.el, "IsModified", self.tag_dict)

    def IsPublishedTextStyle(self):
        """Gets the child objects which have short tag of `IsPublishedTextStyle`, long tag of `IsPublishedTextStyle`"""
        return get_child_object(self.el, "IsPublishedTextStyle", self.tag_dict)

    def Name(self):
        """Gets the child objects which have short tag of `Name`, long tag of `Name`"""
        return get_child_object(self.el, "Name", self.tag_dict)

    def Next(self):
        """Gets the child objects which have short tag of `Next`, long tag of `Next`"""
        return get_child_object(self.el, "Next", self.tag_dict)

    def Rules(self):
        """Gets the child objects which have short tag of `Rules`, long tag of `Rules`"""
        return get_child_object(self.el, "Rules", self.tag_dict)

    def Structure(self):
        """Gets the child objects which have short tag of `Structure`, long tag of `Structure`"""
        return get_child_object(self.el, "Structure", self.tag_dict)

    def Type(self):
        """Gets the child objects which have short tag of `Type`, long tag of `Type`"""
        return get_child_object(self.el, "Type", self.tag_dict)

    def Usage(self):
        """Gets the child objects which have short tag of `Usage`, long tag of `Usage`"""
        return get_child_object(self.el, "Usage", self.tag_dict)

    def UserLevel(self):
        """Gets the child objects which have short tag of `UserLevel`, long tag of `UserLevel`"""
        return get_child_object(self.el, "UserLevel", self.tag_dict)
