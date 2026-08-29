import json
import time
import pytest
from Page_Pom.Negative_POM.register_with_existing_user import existing_user

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_username = user_data["user_base_name"]


@pytest.mark.smoke
def test_register_user(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    login_with_existing_user = existing_user(browserInstance)

    login_with_existing_user.click_on_register_page()
    login_with_existing_user.first_name(user_data["user_first_name"])
    login_with_existing_user.last_name(user_data["user_second_name"])
    login_with_existing_user.address(user_data["user_address"])
    login_with_existing_user.city(user_data["user_city"])
    login_with_existing_user.state(user_data["user_state"])
    login_with_existing_user.zip_code(user_data["user_zip_code"])
    login_with_existing_user.phone(user_data["user_phone_no"])
    login_with_existing_user.ssn(user_data["user_ssn"])
    login_with_existing_user.user_name(user_data["user_base_name"])
    login_with_existing_user.password(user_data["user_password"])
    login_with_existing_user.confirm_password(user_data["user_confirm_password"])
    time.sleep(1)
    login_with_existing_user.click_register()
    time.sleep(4)
    Existing_error_message = f"This username already exists."

    # Assertion
    existing_welcome_error_message = login_with_existing_user.existing_error_message()
    assert existing_welcome_error_message == Existing_error_message, \
        f"Expected '{Existing_error_message}' but got: '{existing_welcome_error_message}'"
    time.sleep(10)