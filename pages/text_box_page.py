import time

from locators.text_box_locators import TextBoxLocators
from pages.base_page import BasePage
from helpers.field_filler import *


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_fields(self):
        full_name = get_random_full_name()
        email = get_random_email()
        current_address = get_random_address()
        perm_address = get_random_address()
        self.is_visible(self.locators.full_name).send_keys(full_name)
        self.is_visible(self.locators.email).send_keys(email)
        self.is_visible(self.locators.current_address).send_keys(current_address)
        self.is_visible(self.locators.permanent_address).send_keys(perm_address)
        self.is_visible(self.locators.submit).click()
        return full_name, email, current_address, perm_address

    def check_output(self):
        full_name = self.is_present(self.locators.created_full_name).text.split(':')[1]
        email = self.is_present(self.locators.created_email).text.split(':')[1]
        current_address = self.is_present(self.locators.created_current_address).text.split(':')[1]
        perm_address = self.is_present(self.locators.created_permanent_address).text.split(':')[1]
        return full_name, email, current_address, perm_address
