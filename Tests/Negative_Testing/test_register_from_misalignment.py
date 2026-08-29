import json
import time

import pytest
from Page_Pom.Negative_POM.Register_field_misaligned import field_misaligned

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["Wrong_credentials"]


user_data = test_list[0]
@pytest.mark.smoke
def test_register_from_misalignment(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    wrong_alignment = field_misaligned(browserInstance)
    wrong_alignment .enter_username(user_data["wrong_username"])
    wrong_alignment .enter_password(user_data["wrong_password"])
    wrong_alignment .click_on_submit()
    # Verify fields alignment (visual UI check)
    username_y, password_y = wrong_alignment.get_field_positions()
    assert abs(username_y - password_y) < 10, "BUG-102: Field alignment issue on login form"



