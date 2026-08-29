import json
import time
from selenium.webdriver.support.ui import Select

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text
from Page_Pom.Positive_POM.open_saving_account import saving_account
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
    making_saving_account = saving_account(browserInstance)
    making_saving_account.click_on_account()
    time.sleep(5)
    making_saving_account.select_saving_account("SAVINGS")
    time.sleep(5)

    making_saving_account.create_saving_account()
    '''
    parent_text = making_saving_account.account_creation()
    print("checking",parent_text)

    assert parent_text.strip() == f"Account Opened!"
    parent_text_1 = making_saving_account.account_creation_1()

    assert parent_text_1.strip() == f"Congratulations, your account is now open."
    print("checking_2",parent_text_1)
    parent_text_2 = making_saving_account.account_creation_2()
    print("checking_3",parent_text_2)

    parent_text_2.strip() == f"Your new account number:"
    time.sleep(10)
'''


