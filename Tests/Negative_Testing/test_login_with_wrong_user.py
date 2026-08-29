import json
import time

import pytest
from Page_Pom.Negative_POM.login_with_wrong_user import wrong_user

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["Wrong_credentials"]


user_data = test_list[0]


@pytest.mark.smoke
def test_register_user(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    wrong_user_login = wrong_user(browserInstance)
    wrong_user_login.wrong_userID(user_data["wrong_username"])
    wrong_user_login.wrong_password(user_data["wrong_password"])
    wrong_user_login.click_on_submit()
    time.sleep(4)
    Error_note = f"Error!\nThe username and password could not be verified."
#Error!

    # Assertion
    Error_message = wrong_user_login.error_message()
    assert Error_message.strip() == Error_note.strip(), \
        f"Expected '{Error_note}' but got: '{Error_message}'""BUG-103: Field alignment issue on login form"""
    print(Error_note)
    print(Error_message)