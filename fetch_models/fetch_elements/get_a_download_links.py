import time
import re
from selenium.webdriver.common.by import By

def get_all_download_links(driver):
    """
    Collect all actual download links from image links and their target pages.

    Args:
    ----
    driver : WebDriver
        The Selenium WebDriver instance.

    Returns:
    -------
    list
        A list containing all download links (hrefs) collected.
    """
    # Step 1: Find all image links (links containing <img> tags)
    image_links = [
        a.get_attribute('href') for a in driver.find_elements(By.TAG_NAME, 'a')
        if a.get_attribute('href') and a.find_elements(By.XPATH, ".//img")
    ]
    print(f"Found {len(image_links)} potential download pages.")

    # Step 2: Initialize list for download links
    main_download_links = []

    # Step 3: Iterate through each image link
    for page_idx, page_link in enumerate(image_links, start=1):
        try:
            print(f"Navigating to download page {page_idx}: {page_link}")

            # Open the link in a new tab
            driver.execute_script("window.open(arguments[0]);", page_link)
            driver.switch_to.window(driver.window_handles[-1])

            # Allow time for the page to load
            time.sleep(5)  # Adjust as necessary

            # Step 4: Collect all <a> and <button> tags with "download" in href or text
            download_elements = driver.find_elements(By.XPATH, "//a[@href] | //button[@href]")
            page_download_links = [
                elem.get_attribute('href') for elem in download_elements
                if re.search(r'\bdownload\b', elem.get_attribute('href') or '', re.IGNORECASE) or
                   re.search(r'\bdownload\b', elem.text or '', re.IGNORECASE)
            ]

            # Save collected links to main_download_links
            main_download_links.extend(page_download_links)
            print(f"Found {len(page_download_links)} download link(s) on page {page_idx}.")

            # Close the current tab and switch back to the main tab
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"Error processing page {page_idx}: {e}")
            continue

    print(f"Total download links collected: {len(main_download_links)}")
    return main_download_links