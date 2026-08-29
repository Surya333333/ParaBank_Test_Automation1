import json
import time
from selenium.webdriver.support.ui import Select
import pytest
from Page_Pom.Positive_POM.open_checking_account import checking_Account
from Page_Pom.Positive_POM.login import Login_user

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


user_data = test_list[0]


@pytest.mark.smoke
def test_register_user(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    Login_user_check = Login_user(browserInstance)
    Login_user_check.enter_login_name(user_data["user_base_name"])
    Login_user_check.enter_login_password(user_data["user_confirm_password"])
    Login_user_check.click_on_submit_button()
    checking_account_create = checking_Account(browserInstance)
    checking_account_create.open_account()
    account_selection =checking_account_create.select_saving_account()
    money_selection = checking_account_create.select_amount()
    print(account_selection)
    checking_account_create.create_saving_account()
    message = checking_account_create.successfully_message()
    print(message)
    assert message == "Account Opened!"



