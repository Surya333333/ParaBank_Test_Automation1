import json
import time

import pytest
from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Positive_POM.request_loan import Request_Loan
test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_username = user_data["user_base_name"]
@pytest.mark.smoke
def test_Request_loan(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()

    login_user = Login_user(browserInstance)
    login_user.enter_login_name(user_data["user_base_name"])
    login_user.enter_login_password(user_data["user_confirm_password"])
    login_user.click_on_submit_button()

    loan_request = Request_Loan(browserInstance)
    loan_request.click_on_request_loan()
    loan_request.enter_loan_amount(user_data["loan_amount"])
    loan_request.down_payment(user_data["down_payment"])
    loan_request.select_account()
    loan_request.click_button_on_request()
    time.sleep(10)