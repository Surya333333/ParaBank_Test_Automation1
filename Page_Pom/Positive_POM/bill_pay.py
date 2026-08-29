from Utils.locators import Locators
import allure
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select

class Bill_Pay:
    def __init__(self,driver):
        self.driver= driver

    @allure.step("Click on Bill Pay menu")
    def bill_pay(self):
        safe_click(self.driver,Locators.bill_pay_click)

    @allure.step("Enter payee name: {payee_name_1}")
    def payee_name(self,payee_name_1):
        safe_send_keys(self.driver,Locators.payee,payee_name_1)
        return payee_name_1

    @allure.step("Enter address: {user_address}")
    def address(self,user_address):
        safe_send_keys(self.driver,Locators.payee_address,user_address)
    @allure.step("Enter City Name: {user_city}")
    def payee_city(self,user_city):
        safe_send_keys(self.driver,Locators.payee_city,user_city)

    @allure.step("Enter State Name: {user_state}")
    def payee_state(self,user_state):
        safe_send_keys(self.driver,Locators.payee_state,user_state)

    @allure.step("Enter zip_code: {user_zip_code}")
    def payee_zipcode(self,user_zip_code):
        safe_send_keys(self.driver,Locators.payee_zipcode,user_zip_code)

    @allure.step("Enter payee phone number: {payee_contact}")
    def payee_phone_number(self,payee_contact):
        safe_send_keys(self.driver,Locators.payee_number,payee_contact)

    @allure.step("Enter payee account number: {Account_Number}")
    def payee_account_number(self,Account_Number):
        safe_send_keys(self.driver,Locators.payee_account,Account_Number)

    @allure.step("Confirm account number: {Confirm_account_number}")
    def payee_confirm_account_number(self,Confirm_account_number):
        safe_send_keys(self.driver,Locators.payee_confirm_account,Confirm_account_number)

    @allure.step("Enter Amount: {Transfer_amount}")
    def amount(self,Transfer_amount):
        safe_send_keys(self.driver,Locators.amount,Transfer_amount)
        return Transfer_amount

    @allure.step("Select account to send money from")
    def select_account_to_send(self,SELECTED = None):
        return safe_select(self.driver,Locators.select_account,SELECTED)

    @allure.step("Click Send Money")
    def Send_money(self):
        safe_click(self.driver,Locators.send_money)

    @allure.step("Get confirmation message")
    def display_message(self):
        return safe_get_text(self.driver,Locators.bill_payment_message)

    @allure.step("Click on submit button ")
    def contact_submit_button(self):
        safe_click(self.driver,Locators.contact_send_button)
