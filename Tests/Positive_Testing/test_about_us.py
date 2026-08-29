import json
from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Positive_POM.about_us import About_us
import pytest
test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


user_data = test_list[0]


@pytest.mark.smoke
def test_about_us(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    login_user = Login_user(browserInstance)
    login_user.enter_login_name(user_data["user_base_name"])
    login_user.enter_login_password(user_data["user_confirm_password"])
    login_user.click_on_submit_button()
    check_about_us = About_us(browserInstance)
    check_about_us.about_us()



