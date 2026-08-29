import json
import time
import pytest
from Page_Pom.Positive_POM.forgot_account import forgot_account


test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]

#if it is not working I will declare this xpassed

@pytest.mark.smoke
def test_forgot_account(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    user_forgot_network = forgot_account(browserInstance)
    user_forgot_network.click_on_forgot()
    user_forgot_network.first_name(user_data["user_first_name"])
    user_forgot_network.last_name(user_data["user_second_name"])
    user_forgot_network.forgot_address(user_data["user_address"])
    user_forgot_network.city(user_data["user_city"])
    user_forgot_network.forgot_state(user_data["user_state"])
    user_forgot_network.zip_code(user_data["user_zip_code"])
    user_forgot_network.forgot_ssn(user_data["user_ssn"])
    user_forgot_network.forgot_button()
    time.sleep(3)
    compare = user_forgot_network.right_panel()
    welcome_message = f"Customer Lookup \nYour login information was located successfully. You are now logged in.\n Username: parasoft\n Password: demo"
    print(compare)

    assert compare.strip() == welcome_message.strip(), \
            f"Expected '{compare}' but got: '{welcome_message}'"


