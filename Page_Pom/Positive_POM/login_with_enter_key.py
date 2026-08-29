from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text
from Utils.locators import Locators
import allure
from selenium.webdriver.common.keys import Keys

class Login_with_enter_key:

    def __init__(self, driver):
        self.driver = driver
    @allure.step(" Enter User Name : {user_name_1}")
    def enter_user_name(self,user_name_1):
        safe_send_keys(self.driver, Locators.login_username,user_name_1)

    @allure.step(" Enter User Password : {user_password}")
    def enter_password(self,user_password):
        element = safe_send_keys(self.driver,Locators.login_password,user_password)
        return element


    @allure.step(" Press Enter to Login ")
    def press_enter_to_login(self, username_1, user_password):
        self.enter_user_name(username_1)
        password_field = self.enter_password(user_password)
        password_field.send_keys(Keys.RETURN)