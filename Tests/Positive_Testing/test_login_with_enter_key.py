import pytest
import json
import time
from Page_Pom.Positive_POM.login_with_enter_key import Login_with_enter_key
test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]

@pytest.mark.smoke
def test_login_with_enter_key(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    login_with_enter_key = Login_with_enter_key(browserInstance)

    login_with_enter_key.press_enter_to_login("Sachin121111@","Sachin121111@")
