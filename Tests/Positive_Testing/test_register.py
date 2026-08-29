import json
import time
import pytest
from Page_Pom.Positive_POM.register import Register


test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_username = user_data["user_base_name"]

@pytest.mark.parametrize(
    "data",
    test_list,   # this comes from test_data["data"]
    ids=[d["user_base_name"] for d in test_list]
)
@pytest.mark.smoke
@pytest.mark.parametrized
def test_register_user(browserInstance,data):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    registration = Register(browserInstance)
    registration.click_on_register_page()
    unique_username = f"{data['user_base_name']}" #_{int(time.time())}
    registration.first_name(data["user_first_name"])
    registration.last_name(data["user_second_name"])
    registration.address(data["user_address"])
    registration.city(data["user_city"])
    registration.state(data["user_state"])
    registration.zip_code(data["user_zip_code"])
    registration.phone(data["user_phone_no"])
    registration.ssn(data["user_ssn"])
    registration.user_name(unique_username)
    registration.password(data["user_password"])
    registration.confirm_password(data["user_confirm_password"])
    time.sleep(1)
    registration.click_register()
    time.sleep(4)
    # Build expected welcome text dynamically
    expected_text = (
        f"Welcome {unique_username}\nYour account was created successfully. You are now logged in."
    )
    # Assertion
    welcome_message = registration.welcome_note()
    assert welcome_message.strip() == expected_text.strip(), \
        f"Expected '{expected_text}' but got: '{welcome_message}'"


