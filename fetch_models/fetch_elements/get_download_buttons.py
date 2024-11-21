import re
from selenium.webdriver.common.by import By

def get_download_buttons(driver):
    all_buttons = driver.find_elements(By.TAG_NAME, 'button')
    print(f'Length of all_buttons: {len(all_buttons)}')

    for idx, button in enumerate(all_buttons, start=1):
        try:
            # Get and strip the text content
            button_text = button.text.strip()
            print(f"Button {idx}: '{button_text}'")
        except Exception as e:
            # Handle any errors that might occur
            print(f"Error retrieving text from button {idx}: {e}")

    # Filter buttons with "download" in text or attributes (case-insensitive)
    download_buttons = [
        button for button in all_buttons
        if re.search(r'\bdownload\b', (button.text or ""), re.IGNORECASE) or
           re.search(r'\bdownload\b', (button.get_attribute("id") or ""), re.IGNORECASE) or
           re.search(r'\bdownload\b', (button.get_attribute("name") or ""), re.IGNORECASE) or
           re.search(r'\bdownload\b', (button.get_attribute("title") or ""), re.IGNORECASE) or
           re.search(r'\bdownload\b', (button.get_attribute("value") or ""), re.IGNORECASE)
    ]

    # Debug: Print the text and attributes of each button identified as a download button
    for idx, button in enumerate(download_buttons, start=1):
        print('Inside buttons')
        button_text = button.text.strip()
        button_id = button.get_attribute("id") or ""
        button_name = button.get_attribute("name") or ""
        button_title = button.get_attribute("title") or ""
        button_value = button.get_attribute("value") or ""
        
        print(f"Download Button {idx}: Text='{button_text}', ID='{button_id}', "
              f"Name='{button_name}', Title='{button_title}', Value='{button_value}'")

    print(f"Total download buttons found: {len(download_buttons)}")
    return download_buttons