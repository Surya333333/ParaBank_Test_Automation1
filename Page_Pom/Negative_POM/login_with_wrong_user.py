from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys
from Utils.locators import Locators
import allure
class wrong_user:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Try login with wrong user name :{existing_username} ")
    def wrong_userID(self,existing_username):
        safe_send_keys(self.driver,Locators.login_username,existing_username)

    @allure.step("Enter user wrong password :{password} ")
    def wrong_password(self,password):
        safe_send_keys(self.driver,Locators.login_password,password)

    @allure.step("Click on Submit button ")
    def click_on_submit(self):
        safe_click(self.driver,Locators.login_submit)

    @allure.step("Error message displayed ")
    def error_message(self):
        return safe_get_text(self.driver,Locators.error_note)
