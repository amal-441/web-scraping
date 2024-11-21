from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from selenium.common.exceptions import StaleElementReferenceException
from login.webdriver_manager import WebDriverManager
import re
import json
import os

# Use Service to set the executable path for the WebDriver
# service = Service("./chromedriver/chromedriver.exe")  # Set the correct path to chromedriver here
wd = WebDriverManager.get_instance().get_driver()



def gather_image_links(body_element):
       
    # Gather href links from <a> tags around each <img> element
    # Get the current page URL
    current_page_url = wd.current_url
    print("current page url :",current_page_url)
    href_links = []
    # Locate all image elements with the 'previewImage' class
    img_elements = body_element.find_elements(By.TAG_NAME, 'img')
    print(f"Found {len(img_elements)} <img> element(s) within body_element.")
    for idx, img in enumerate(img_elements):
        try:
            # Locate all ancestor <a> tags with href attributes for the current <img> element
            ancestor_a_tags = img.find_elements(By.XPATH, './ancestor::a[@href]')        
            # Collect hrefs and outerHTML for each ancestor <a> tag
            for a_idx, ancestor_a in enumerate(ancestor_a_tags):
                href_link = ancestor_a.get_attribute("href")
                # Clean up the URL by removing fragment identifiers
            if href_link:
                cleaned_href = href_link.split('#')[0]  # Remove everything after the fragment
                if cleaned_href and cleaned_href != current_page_url:
                    # Avoid duplicates by checking if the link is already in the list
                    if cleaned_href not in href_links:
                        href_links.append(cleaned_href)
                        print(f"Collected href link: {cleaned_href}")
                    else:
                        print(f"Skipped duplicate href: {cleaned_href}")
                else:
                    print(f"Skipped self-link or empty href: {cleaned_href}")
            else:
                print("Empty href attribute found.")
    
        except Exception as e:
            print(f"Error processing image {idx + 1}: {e}")
    # Ensure href_links is populated before calling the function
    return href_links
