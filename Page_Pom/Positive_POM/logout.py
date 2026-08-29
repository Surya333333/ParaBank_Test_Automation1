from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_select,safe_send_keys
import allure

class Logout:
    def __init__(self,driver):
        self.driver = driver
    @allure.step("Click on Logout Button:")
    def logout(self):
        safe_click(self.driver,Locators.logout_button)
