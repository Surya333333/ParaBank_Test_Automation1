import pytest
import time
from Page_Pom.Positive_POM.account_overview_check import overview_check
from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Positive_POM.account_overview import account_overview
import json

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


user_data = test_list[0]


@pytest.mark.smoke
def test_account_over_view(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    user_login = Login_user(browserInstance)
    user_login.enter_login_name(user_data["user_base_name"])
    user_login.enter_login_password(user_data["user_confirm_password"])
    user_login.click_on_submit_button()
    overview_accounts = overview_check(browserInstance)
    check_accounts = overview_accounts.user_account_overview
    print(check_accounts)
    time.sleep(12)