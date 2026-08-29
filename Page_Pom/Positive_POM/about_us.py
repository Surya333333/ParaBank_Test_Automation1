from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
from Utils.locators import Locators
import allure

class About_us:
    def __init__(self,driver):
        self.driver = driver

    @allure.step(" Click on About Us Page ")
    def click_on(self):
        safe_click(self.driver,Locators.click_on)
    @allure.step(" About Us Page ")
    def about_us(self):
        return safe_get_text(self.driver,Locators.about_us)