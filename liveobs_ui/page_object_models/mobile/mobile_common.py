"""
Common Functionality for Mobile
This class contains common functionality for the mobile frontend such as:
- navigating to a particular URL
"""
from liveobs_ui.selectors.menu_selectors import TASK_ITEM, PATIENT_ITEM, \
    LOGOUT_BUTTON
from liveobs_ui.selectors.list import LIST_CONTAINER
from liveobs_ui.page_object_models.common.base_liveobs_page import \
    BaseLiveObsPage


class BaseMobilePage(BaseLiveObsPage):
    """
        Base class to initialise the base page
        that will be called from all pages
    """

    def go_to_task_list(self):
        """
            Navigate to the task list
        """
        task_list_item = self.driver.find_element(*TASK_ITEM)
        self.click_and_verify_change(task_list_item, LIST_CONTAINER)

    def go_to_patient_list(self):
        """
            Navigate to the patient list
        """
        patient_list_item = \
            self.driver.find_element(*PATIENT_ITEM)
        self.click_and_verify_change(patient_list_item, LIST_CONTAINER)

    def is_task_list(self):
        """
        Are we on the task list?

        :return: If current URL is the task list URL
        :rtype: bool
        """
        return '/tasks' in self.driver.current_url

    def is_patient_list(self):
        """
        Are we on the patient list?

        :return: If current URL is the patient list URL
        :rtype: bool
        """
        return '/patients' in self.driver.current_url

    def logout(self):
        """
            Log out of the app
        """
        logout = self.driver.find_element(*LOGOUT_BUTTON)
        logout.click()