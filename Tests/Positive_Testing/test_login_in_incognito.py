import pytest
import json
import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from Page_Pom.Positive_POM.login_in_incognito import login_in_incognito_mode
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_login_in_incognito(browserInstance):
    driver = browserInstance

    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    login_in_incognito = login_in_incognito_mode(driver)
    login_in_incognito.enter_login_name(user_data["user_base_name"])
    login_in_incognito.enter_login_password(user_data["user_confirm_password"])
    login_in_incognito.click_on_submit_button()
    time.sleep(10)
