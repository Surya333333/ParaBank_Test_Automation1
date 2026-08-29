import pytest
import json


from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Positive_POM.account_overview import account_overview
test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


user_data = test_list[0]


@pytest.mark.smoke
def test_account_over_view(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    login_account = Login_user(browserInstance)
    login_account.enter_login_name(user_data["user_base_name"])
    login_account.enter_login_password(user_data["user_confirm_password"])
    login_account.click_on_submit_button()
    overview = account_overview(browserInstance)
    message = overview.account_overview()
    print(message)
    assert "Accounts Overview" in message




