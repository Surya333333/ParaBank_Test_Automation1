import json
import time
import pytest
from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Positive_POM.contact_us import Contact_us
test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


user_data = test_list[0]
@pytest.mark.smoke
def test_contact_us(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    user_login = Login_user(browserInstance)
    user_login.enter_login_name(user_data["user_base_name"])
    user_login.enter_login_password(user_data["user_confirm_password"])
    user_login.click_on_submit_button()


    fill_contact_us_form = Contact_us(browserInstance)
    fill_contact_us_form.click_on_contact_us()
    user_name = fill_contact_us_form.contact_name(user_data["user_first_name"])
    fill_contact_us_form.contact_phone(user_data["user_phone_no"])
    fill_contact_us_form.contact_email(user_data["contact_email_name"])
    fill_contact_us_form.contact_message(user_data["message"])
    fill_contact_us_form.submit_button()
    time.sleep(10)
    console_message = fill_contact_us_form.message()
    display_message = (
        f"Customer Care\n"
        f"Thank you {user_name}\n"
        f"A Customer Care Representative will be contacting you."
    )
    assert console_message == display_message, \
        f"Expected '{console_message}' but got: '{display_message}'"
