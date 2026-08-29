from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_select,safe_send_keys
import allure

class overview_check:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Check for user Active account")
    def user_account_overview(self):
        return safe_get_text(self.driver,Locators.user_accounts)

