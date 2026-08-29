from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_select,safe_get_text,safe_send_keys
import allure

class account_overview:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on overview button ")
    def click_on_overview(self):
        safe_click(self.driver,Locators.overview)

    @allure.step("Account Overview")
    def account_overview(self):
        return safe_get_text(self.driver,Locators.tittle_compare)
