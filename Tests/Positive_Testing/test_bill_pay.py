import json
import pytest
import time

from Page_Pom.Positive_POM.bill_pay import Bill_Pay
from Page_Pom.Positive_POM.login import Login_user

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


user_data = test_list[0]
@pytest.mark.smoke
def test_Bill_Pay(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()

    # Step 1: Login
    login_user = Login_user(driver)
    login_user.enter_login_name(user_data["user_base_name"])
    login_user.enter_login_password(user_data["user_confirm_password"])
    login_user.click_on_submit_button()

    bill_pay_page = Bill_Pay(driver)
    bill_pay_page.bill_pay()
    payee_name = bill_pay_page.payee_name(user_data["payee_name"])
    print(payee_name)
    bill_pay_page.payee_phone_number(user_data["Payee_contact_details"])
    bill_pay_page.payee_account_number(user_data["Account_number"])
    bill_pay_page.payee_confirm_account_number(user_data["Confirm_account_number"])
    bill_pay_page.address(user_data["user_address"])
    bill_pay_page.payee_city(user_data["user_city"])
    bill_pay_page.payee_zipcode(user_data["user_zip_code"])
    bill_pay_page.payee_state(user_data["user_state"])
    bill_pay_page.payee_zipcode(user_data["user_zip_code"])
    send_money = bill_pay_page.amount(user_data["Transfer_Account"])
    print(send_money)
    from_account = bill_pay_page.select_account_to_send()
    bill_pay_page.Send_money()
    time.sleep(30)
    console_message = bill_pay_page.display_message()


    display_message = (
    f"Bill Payment Complete\n"
    f"Bill Payment to {payee_name} in the amount of ${int(user_data['Transfer_Account']):}.00 from account {from_account} was successful.\n"
    f"See Account Activity for more details."
        )

    assert console_message == display_message, \
    f"Expected '{console_message}' but got: '{display_message}'"












