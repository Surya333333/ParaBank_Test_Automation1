from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_select,safe_send_keys
import allure


class forgot_new_account:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Account overview")
    def account_check(self):
        return safe_get_text(self.driver,Locators.Right_panel)

