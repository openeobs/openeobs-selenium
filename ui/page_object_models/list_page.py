"""
Page Object Model for List Page
The List Page is a base class for the task and patient lists as they use the
same template to render content
"""
from ui.page_object_models.mobile_common import BaseMobilePage
from ui.selectors.list import LIST_ITEM


class ListPage(BaseMobilePage):
    """
    Class that handles generic list page functionality
    """

    def get_list_items(self):
        """
        Get a list of the items in the task / patient list

        :return: A list of ``a`` tags from the list
        :rtype: list
        """
        return self.driver.find_elements(*LIST_ITEM)

    def get_list_item(self, text_to_find):
        """
        Get a specific item from the list

        :param text_to_find: Text that should be in the list item to be found
        :type text_to_find: str
        :return: The list item if found or None
        """
        list_items = self.get_list_items()
        list_item = [el for el in list_items if text_to_find in el.text]
        if list_item:
            return list_item[0]
        return None