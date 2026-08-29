from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys
from Utils.locators import Locators
import allure

class existing_user:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on register page ")
    def click_on_register_page(self):
        safe_click(self.driver,Locators.register)

    @allure.step("Enter exiting user first name :{user_first_name}")
    def first_name(self,user_first_name):
        safe_send_keys(self.driver,Locators.first_name,user_first_name)

    @allure.step("Enter exiting user last name :{user_last_name}")
    def last_name(self,user_last_name):
        safe_send_keys(self.driver,Locators.last_name,user_last_name)

    @allure.step("Enter exiting user address: {user_address}")
    def address(self,user_address):
        safe_send_keys(self.driver,Locators.address,user_address)

    @allure.step("Enter exiting user city: {user_city}")
    def city(self,user_city):
        safe_send_keys(self.driver,Locators.city,user_city)

    @allure.step("Enter exiting user state: {user_state}")
    def state(self,user_state):
        safe_send_keys(self.driver,Locators.state,user_state)

    @allure.step("Enter exiting user zipcode : {user_zip_code}")
    def zip_code(self,user_zip_code):
        safe_send_keys(self.driver,Locators.zip_code,user_zip_code)

    @allure.step("Enter exiting user phone number: {user_phone_no}")
    def phone(self,user_phone_no):
        safe_send_keys(self.driver,Locators.phone_number,user_phone_no)

    @allure.step("Enter exiting user SSN : {user_ssn}")
    def ssn(self,user_ssn):
        safe_send_keys(self.driver,Locators.ssn_number,user_ssn)

    @allure.step("Enter exiting existing user name: {user_name}")
    def user_name(self,user_name):
        safe_send_keys(self.driver,Locators.user_name_id,user_name)

    @allure.step("Enter exiting user password: {user_password}")
    def password(self,user_password):
        safe_send_keys(self.driver,Locators.password,user_password)

    @allure.step("Enter exiting user confirm password: {user_confirm_password}")
    def confirm_password(self,user_confirm_password):
        safe_send_keys(self.driver,Locators.confirm_password,user_confirm_password)

    @allure.step("Click on register button")
    def click_register(self):
        safe_click(self.driver,Locators.register_button)

    @allure.step("Message showed after registration ")
    def existing_error_message(self):
        return safe_get_text(self.driver,Locators.existing_user_error)

