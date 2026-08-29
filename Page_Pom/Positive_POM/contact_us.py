from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
import allure

class Contact_us:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on Contact us page")
    def click_on_contact_us(self):
        safe_click(self.driver,Locators.contact)

    @allure.step("Enter user name: {user_first_name}")
    def contact_name(self,user_first_name):
        safe_send_keys(self.driver,Locators.contact_name,user_first_name)
        return user_first_name

    @allure.step("Enter user email: {contact_email_name}")
    def contact_email(self,contact_email_name):
        safe_send_keys(self.driver,Locators.contact_email,contact_email_name)

    @allure.step("Enter user phone number: {user_phone_no}")
    def contact_phone(self,user_phone_no):
        safe_send_keys(self.driver,Locators.contact_phone,user_phone_no)

    @allure.step("Message Typed by user: {message}")
    def contact_message(self,message):
        safe_send_keys(self.driver,Locators.contact_message,message)

    @allure.step("Click on submit button")
    def submit_button(self):
        safe_click(self.driver,Locators.contact_send_button)

    @allure.step("Message shown after submission: {welcome_note}")
    def message(self):
        return safe_get_text(self.driver,Locators.welcome_note)
