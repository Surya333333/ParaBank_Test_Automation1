import json
import time
import pytest
from Page_Pom.Positive_POM.login import Login_user


# Load login data
with open(r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json') as f:
    test_data = json.load(f)
    login_data = test_data["login_data"]


@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("creds", login_data)
def test_login_user(browserInstance, creds):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()

    login = Login_user(driver)
    login.enter_login_name(creds["user_name_1"])
    login.enter_login_password(creds["user_password"])
    login.click_on_submit_button()
    time.sleep(3)

    # Add validation — you can check element visibility or welcome text
    assert "overview" in driver.current_url.lower(), "Login failed — not redirected to account overview."
