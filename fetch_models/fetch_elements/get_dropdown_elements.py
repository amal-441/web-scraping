
def get_dropdown_download_buttons(driver):
    # Locate the <ul> element with the class 'dropdown-menu'
    try:
        dropdown_menu = driver.find_element(By.CLASS_NAME, 'dropdown-menu')
    except Exception as e:
        print(f"Dropdown menu not found: {e}")
        return []
    
    # Find all <li> elements inside <ul> with class 'download'
    dropdown_items = dropdown_menu.find_elements(By.CSS_SELECTOR, 'li.download')
    print(f"Found {len(dropdown_items)} download item(s) in the dropdown.")
    
    # Debug: Print the text of each dropdown item identified as a download item
    for idx, item in enumerate(dropdown_items, start=1):
        try:
            item_text = item.text.strip()
            print(f"Dropdown Download Item {idx} text: '{item_text}'")
        except Exception as e:
            print(f"Error retrieving text from dropdown item {idx}: {e}")
    
    # Return the filtered list of download items
    return dropdown_items