import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json



from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException,
)
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text
from Utils.locators import Locators

test_data_path = r'C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


def run_all():
    pytest.main([
        "-v",
        "-s",
        "tests"
        ])
if __name__ == "__main__":
    run_all()