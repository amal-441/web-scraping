from selenium.webdriver.common.by import By
import re

def get_download_inputs(driver):
    download_inputs = [
        input_tag for input_tag in driver.find_elements(By.TAG_NAME, 'input')
        if re.search(r'\b[Dd]ownload\b', input_tag.get_attribute('value') or '') or
           re.search(r'\b[Dd]ownload\b', input_tag.get_attribute('name') or '') or
           re.search(r'\b[Dd]ownload\b', input_tag.get_attribute('id') or '') or
           re.search(r'\b[Dd]ownload\b', input_tag.get_attribute('title') or '')
    ]
    print(f"Found {len(download_inputs)} potential download input(s).")
    return download_inputs