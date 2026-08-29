import time
import os

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utils.locators import Locators



def capture_screenshot(driver, screenshot_name, folder_name="capture_screenshot"):
    """
    Captures a screenshot and saves it to the given folder.
    """
    base_dir = os.getcwd()
    screenshot_dir = os.path.join(base_dir, folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Add timestamp to avoid overwriting
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(screenshot_dir, f"{screenshot_name}_{timestamp}.png")

    driver.get_screenshot_as_file(file_path)
    print(f"✅ Screenshot saved at: {file_path}")

    return file_path



def safe_click(driver, xpath, timeout=30):
    for _ in range(3):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            ).click()
            break
        except StaleElementReferenceException:
            time.sleep(10)

def safe_send_keys(driver, xpath, value, timeout=30):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.clear()
    element.send_keys(value)
    return element


def safe_get_text(driver, xpath, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).text


def safe_select(driver, xpath, value, by="text", timeout=30):
    for _ in range(3):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            select = Select(element)
            if value is None:

                return select.first_selected_option.text

            if by == "text":
                select.select_by_visible_text(value)
            elif by == "value":
                select.select_by_value(value)
            elif by == "index":
                select.select_by_index(int(value))
            return select.first_selected_option.text
        except StaleElementReferenceException:
            time.sleep(2)

def safe_get_location(driver, xpath, axis='y', timeout=30, retries=3):
        """
        Safely get the x or y location of a web element.
        axis = 'x' or 'y' (default 'y')
        """
        for attempt in range(retries):
            try:
                # Wait for element presence
                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                location = element.location

                # Return requested coordinate
                if axis.lower() == 'x':
                    return location['x']
                elif axis.lower() == 'y':
                    return location['y']
                else:
                    raise ValueError("Axis must be either 'x' or 'y'")

            except StaleElementReferenceException:
                print(f"[Retry {attempt + 1}] Element became stale, retrying...")
                time.sleep(2)

            except TimeoutException:
                print(f"[Timeout] Element not found for xpath: {xpath}")
                break

        raise Exception(f"safe_get_location failed after {retries} attempts for xpath: {xpath}")

