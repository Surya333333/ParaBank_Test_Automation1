import json
import time
from datetime import datetime
import pytest
from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Negative_POM.Request_loan_with_high_amount import Request_Highest_Loan
test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_username = user_data["user_base_name"]
@pytest.mark.smoke
def test_Request_Highest_loan(browserInstance,creds):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()

    login_user = Login_user(browserInstance)
    login_user.enter_login_name(creds["user_name_1"])
    login_user.enter_login_password(creds["user_password"])
    login_user.click_on_submit_button()

    loan_request = Request_Highest_Loan(browserInstance)
    loan_request.click_on_request_loan()
    loan_request.enter_loan_amount(user_data["high_amount_loan"])
    loan_request.down_payment(user_data["down_payment"])
    loan_request.select_account()
    loan_request.click_button_on_request()
    '''
    first_Message = loan_request.loan_request_proceed()
    second_message = loan_request.loan_provider()
    third_message = loan_request.loan_date()
    fourth_message = loan_request.loan_status()
    fifth_message = loan_request.loan_error()
    display_message = "We cannot grant a loan in that amount with your available funds."

    assert fifth_message.strip() == display_message.strip(), \
        f"Expected '{fifth_message}' but got: '{display_message}'"
    
    today_date = datetime.now().strftime("%m-%d-%Y")
    print(today_date)
    '''
    '''
    assert first_Message.strip() == "Loan Request Processed"
    assert "Wealth Securities Dynamic Loans (WSDL)" in second_message
    assert third_message.strip() == today_date
    assert fourth_message.strip() == "Denied"
    

    #assert "We cannot grant a loan in that amount with your available funds." in fifth_message
    print(fifth_message)
    '''
    time.sleep(100)