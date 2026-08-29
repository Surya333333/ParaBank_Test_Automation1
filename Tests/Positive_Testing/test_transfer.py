from Page_Pom.Positive_POM.login import Login_user
from Page_Pom.Positive_POM.transfer_funds import transfer
import json
import time
import pytest

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
money_send = user_data["send_money"]

@pytest.mark.smoke
def test_transfer(browserInstance):
    driver = browserInstance
    browserInstance.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    login_user = Login_user(browserInstance)
    login_user.enter_login_name(user_data["user_base_name"])
    login_user.enter_login_password(user_data["user_confirm_password"])
    login_user.click_on_submit_button()
    transfer_account = transfer(browserInstance)
    transfer_account.click_on_transfer_button()
    transfer_account.money_transfer(user_data["send_money"])
    from_acc = transfer_account.from_account()
    to_acc = transfer_account.to_account()
    transfer_account.click_on_transfer()

    print(f"Transferred from {from_acc} to {to_acc}")
    time.sleep(12)
    message = transfer_account.transfer_message_show()
    display_message = (
        f"Transfer Complete!\n"
        f"${int(user_data['send_money']):}.00 has been transferred from account #{from_acc} to account #{to_acc}.\n"
        f"See Account Activity for more details."
    )

    assert message.strip() == display_message.strip(), \
        f"Expected '{message}' but got: '{display_message}'"
