from Utils.selenium_helpers import safe_click, safe_send_keys,safe_get_location
from Utils.locators import Locators
import allure
class field_misaligned:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Enter username :{existing_username} ")
    def enter_username(self,existing_username):
        safe_send_keys(self.driver,Locators.login_username,existing_username)

    @allure.step("Enter user password :{password} ")
    def enter_password(self, password):
        safe_send_keys(self.driver, Locators.login_password, password)

    @allure.step("Click on Submit button ")
    def click_on_submit(self):
        safe_click(self.driver, Locators.login_submit)

    # POM
    def get_field_positions(self):
        username_y = safe_get_location(self.driver, Locators.login_username, "y")
        password_y = safe_get_location(self.driver, Locators.login_password, "y")
        return username_y, password_y
