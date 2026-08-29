from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
import allure

class checking_Account:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on open new account")
    def open_account(self):
        safe_click(self.driver,Locators.saving_account)

    @allure.step("Select checking account from dropdown ")
    def select_saving_account(self,selected=None):
        return safe_select(self.driver,Locators.select_saving,selected)

    @allure.step("Select amount to send from dropdown")
    def select_amount(self,selected=None):
        return safe_select(self.driver,Locators.money_selection,selected)

    @allure.step("Click on submit button to make account ")
    def create_saving_account(self):
        safe_click(self.driver,Locators.create_account)

    @allure.step("Displayed message after amount send successfully")
    def successfully_message(self):
        return safe_get_text(self.driver,Locators.successfuly_checking_creation)

