from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
import allure

class Request_Highest_Loan:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on request loan : ")
    def click_on_request_loan(self):
        safe_click(self.driver,Locators.click_on_loan_request)
    @allure.step("Enter the Loan amount: {loan_amount}")
    def enter_loan_amount(self,loan_amount):
        safe_send_keys(self.driver,Locators.loan_amount,loan_amount)
    @allure.step("Enter the down_payment :{down_payment}")
    def down_payment(self,down_payment):
        safe_send_keys(self.driver,Locators.down_payment,down_payment)

    @allure.step("Select the bank account :")
    def select_account(self,SELECTED = None):
        return safe_select(self.driver,Locators.select_account_loan,SELECTED)

    @allure.step("Click on apply loan : ")
    def click_button_on_request(self):
        safe_click(self.driver, Locators.loan_apply)

    @allure.step(" Loan Request Processed ")
    def loan_request_proceed(self):
        return safe_get_text(self.driver,Locators.loan_req)

    @allure.step(" Loan Provider ")
    def loan_provider(self):
        return safe_get_text(self.driver, Locators.loan_provider)

    @allure.step(" Loan Date ")
    def loan_date(self):
        return safe_get_text(self.driver, Locators.loan_date)

    @allure.step(" Loan Status ")
    def loan_status(self):
        return safe_get_text(self.driver, Locators.loan_status)

    @allure.step(" Loan Error ")
    def loan_error(self):
        return safe_get_text(self.driver, Locators.loan_error)




