import json
import pytest
import time
from Page_Pom.Positive_POM.logout import Logout
from Page_Pom.Positive_POM.login import Login_user
from Tests.Positive_Testing.test_register import user_data

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
def test_logout(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    login_user_to_check_for_logout = Login_user(browserInstance)
    login_user_to_check_for_logout.enter_login_name(user_data["user_base_name"])
    login_user_to_check_for_logout.enter_login_password(user_data["user_confirm_password"])
    login_user_to_check_for_logout.click_on_submit_button
    logout_user = Logout(browserInstance)
    logout_user.logout()
    time.sleep(5)
