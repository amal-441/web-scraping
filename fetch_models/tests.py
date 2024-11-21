from django.test import TestCase

# Create your tests here.
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import time
import os
import math
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import re
from rest_framework.decorators import api_view
from utils.login import login_and_save_cookies
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')

# Use Service to set the executable path for the WebDriver
service = Service("./chromedriver/chromedriver.exe")  # Set the correct path to chromedriver here
driver = webdriver.Chrome(service=service, options=options)


# def setup_driver(timeout=180):
#     """
#     Set up and return a Selenium WebDriver instance with specified configurations.

#     Args:
#         timeout (int): Maximum time in seconds to wait for page loads.

#     Returns:
#         WebDriver: A configured Selenium WebDriver instance.
#     """
#     # Configure Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run browser in headless mode
#     chrome_options.add_argument("--window-size=1920x1080")  # Set browser window size
#     chrome_options.add_argument("--disable-notifications")  # Disable browser notifications
#     chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
#     chrome_options.add_argument("--verbose")  # Enable verbose logging
    
#     # Configure download preferences
#     download_folder = r"C:\Users\Lenovo\Downloads"  # Ensure this path exists
#     chrome_options.add_experimental_option("prefs", {
#         "download.default_directory": download_folder,  # Set default download folder
#         "download.prompt_for_download": False,  # Disable download prompt
#         "download.directory_upgrade": True,  # Automatically upgrade the directory
#         "safebrowsing.enabled": True  # Enable safe browsing for downloads
#     })
    
#     # Path to chromedriver executable
#     chromedriver_path = "./chromedriver/chromedriver.exe"  # Update to your actual path
#     if not os.path.exists(chromedriver_path):
#         raise FileNotFoundError(f"Chromedriver not found at: {chromedriver_path}")
    
#     # Initialize the WebDriver with options and service
#     service = Service(chromedriver_path)
#     driver = webdriver.Chrome(service=service, options=chrome_options)
    
#     # Set a timeout for page loading
#     driver.set_page_load_timeout(timeout)

#     # Optional: Add an implicit wait for elements
#     driver.implicitly_wait(10)
    
#     print("Driver setup successful!")
#     return driver

# # Example usage
# driver = setup_driver()
def login_using_cookies(wd, login_url, dashboard_url):
    wd.get(login_url)
    try:
        WebDriverWait(wd, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Page fully loaded!")
    except Exception as e:
        print("Page not loaded within time:", e)
        return None  # Return None if login fails
    
    # Get all form elements on the page
    form_elements = wd.find_elements(By.TAG_NAME, "form")
    print(f"{len(form_elements)} form(s) found!")

    for form_element in form_elements:
        email_input = None
        password_input = None
        submit_button = None

        print("Element is visible? " + str(form_element.is_displayed()))

    
        try:
            email_input = form_element.find_element(
    By.XPATH,
    "//input[("  
    "contains(translate(@id, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'username') or "
    "contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'username') or "
    "contains(translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'username') or "
    "contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'username') or "
    "contains(translate(@id, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'signin') or "
    "contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'signin') or "
    "contains(translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'signin') or "
    "contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'signin') or "
    "contains(translate(@id, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'login') or "
    "contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'login') or "
    "contains(translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'login') or "
    "contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'login') or "
    "translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'text' or "
    "translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'email') or "
    "("
    "contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'email') or "
    "contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'name@email.com') or "
    "contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'username') or "
    "contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'name')"
    ")]"
)
            email_input.send_keys("amaldq333@gmail.com")  # Replace with your actual username
            print("Email Entered")

            password_input = form_element.find_element(
    By.XPATH,
    "//input[" 
    "contains(translate(@id, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'password') or "
    "contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'password') or "
    "@type='password' or "
    "contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'password') or "
    "(@id='password' or @type='password' or @name='password')]"
)
            password_input.send_keys("model.io123")  # Replace with your actual password
            print("Password Entered")

            submit_button = form_element.find_element(By.XPATH, "//*[contains(@type, 'submit') or contains(@value, 'Login') or contains(@value, 'Sign In')]")
            submit_button.click()
            print("Login form submitted.")
        except Exception as e:
            print(f"Error locating login elements: {e}")
            return  # Exit the function if login fails

        # Step 3: Wait for login to complete (use an explicit wait to ensure the login form has been processed)
        time.sleep(5)  # Adjust the sleep time if necessary (to allow login)

        # Step 4: Save cookies after login
        saveCookies(wd)

        # Step 5: Navigate to the dashboard to confirm the login
        wd.get(dashboard_url)  # Navigate to the dashboard page
    
        # Wait for the dashboard page to load completely
        WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        print("Login confirmed and dashboard is accessible!")

        # Get the page title for confirmation
        page_title = wd.title
        print(f"Dashboard Page Title: {page_title}")

        # Step 6: Wait for the dashboard page to load and verify if login was successful
        try:
            WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            print('Login successful')
            return True
        except TimeoutException:
            print("Dashboard loading timed out.")
            return False


@csrf_exempt
@api_view(['POST'])
def fetch_elements_and_download(request):
    try:
        login_url = 'https://app.modelo.io/damf/myspace?locale=en_US'
        dashboard_url = 'https://www.modelo.io/3d-models?hl=en'

        if login_using_cookies(driver,login_url,dashboard_url):
            print("Login Success")
        else:
            print("Login Failed")
        
        print("Login Success!")            
        # Define the cookies path
        cookies_path = os.path.join(settings.BASE_DIR, 'cookies.json')

        # Ensure cookies file exists
        if not os.path.exists(cookies_path):
            print("Cookies file not found. Please log in first.")
            return JsonResponse({'status': 'error', 'message': 'Cookies not found. Please login first.'}, status=400)
   
        time.sleep(5)  # Allow cookies to take effect
        saveCookies(driver)
        driver.get(dashboard_url)

        # Wait for the dashboard page to load completely
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        print("Login confirmed and dashboard is accessible!")

        # Get the page title for confirmation
        page_title = driver.title
        print(f"Dashboard Page Title: {page_title}")

        # After login, navigate to another page to fetch elements and download
        try:
            website = 'https://www.modelo.io/3d-models/?hl=en'
            driver.get(website)
            print(f"Navigating to: {website}")

            # Wait for the page body to confirm the page has loaded
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            print("Page loaded successfully!")

            # Perform scraping logic
            body_element = get_body_element(website, driver)
            href_links = gather_image_links(driver, body_element)
            if href_links:
                # print(f"Collected {len(href_links)} href links. Processing...")
                # search_and_click_download_button(driver,href_links)
                print(f"Collected {len(href_links)} href links. Dividing into chunks and processing sequentially...")
                process_links_sequentially(driver, href_links, download_dir, num_chunks=5)
            else:
                print("No href links found.")
            # search_and_click_download_button(driver, href_links)

            return JsonResponse({'status': 'success', 'message': 'Elements fetched and download triggered successfully'})

        except Exception as scrape_exception:
            print(f"Scraping Error: {scrape_exception}")
            return JsonResponse({'status': 'error', 'message': 'Scraping process failed', 'error': str(scrape_exception)}, status=500)

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'status': 'error', 'message': 'An error occurred', 'error': str(e)}, status=500)
download_dir = "C:\\Users\\Lenovo\\Downloads"


# def search_and_click_download_button(driver, href_links):
#     successful_element_type = None  # Track the element type that successfully triggered download
#     for link in href_links:
#         try:
#             # Navigate to each link and wait for it to load
#             driver.get(link)
#             print(f"Navigated to: {link}")
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
#             # Record the current state of the download directory to detect new downloads
#             before_files = set(os.listdir(download_dir))

#             # If a download type has been successful, only attempt that type
#             if successful_element_type:
#                 elements = get_elements_by_type(driver, successful_element_type)
#                 if attempt_download_from_elements(driver, elements, successful_element_type):
#                     print(f"Download triggered using {successful_element_type}.")
#                     continue  # Skip to the next link
#             # Collect elements only if no successful element type is defined
#             element_checks = [
#                 ("button", get_download_buttons(driver)),
#                 ("img", get_img_elements(driver)),
#                 ("image link", get_image_links(driver)),
#                 ("input", get_download_inputs(driver)),
                
#             ]
#             for element_type, elements in element_checks:
#                 print(f"Attempting {element_type} download!")
#                 if attempt_download_from_elements(driver, elements, element_type):
#                     print(f"Download triggered by {element_type}.")            
#                     successful_element_type = element_type  # Save the successful element type
#                     break  # Exit element checks since download was triggered

#         except TimeoutException:
#             print("Timeout waiting for page load.")
#         except Exception as e:
#             print(f"An error occurred while processing {link}: {e}")

def search_and_click_thread_download(driver, href_links, download_dir):
    successful_element_type = None  # Track the element type that successfully triggered download
    for link in href_links:
        try:
            # Navigate to each link and wait for it to load
            driver.get(link)
            print(f"Navigated to: {link}")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            # Record the current state of the download directory to detect new downloads
            before_files = set(os.listdir(download_dir))

            # If a download type has been successful, only attempt that type
            if successful_element_type:
                elements = get_elements_by_type(driver, successful_element_type)
                if attempt_download_from_elements(driver, elements, successful_element_type, download_dir, before_files):
                    print(f"Download triggered using {successful_element_type}.")
                    continue  # Skip to the next link

            # Collect elements only if no successful element type is defined
            element_checks = [
                ("button", get_download_buttons(driver)),
                ("img", get_img_elements(driver)),
                ("image link", get_image_links(driver)),
                ("input", get_download_inputs(driver)),
            ]

            for element_type, elements in element_checks:
                print(f"Attempting {element_type} download!")
                if attempt_download_from_elements(driver, elements, element_type, download_dir, before_files):
                    print(f"Download triggered by {element_type}.")
                    successful_element_type = element_type  # Save the successful element type
                    break  # Exit element checks since download was triggered

        except TimeoutException:
            print("Timeout waiting for page load.")
        except Exception as e:
            print(f"An error occurred while processing {link}: {e}")


def get_xpath_for_element(element, element_type):
    """Generate an XPath for the element based on its type and attributes."""
    if element_type == "button":
        return ".//button[contains(text(), 'Download') or @class='download']"
    elif element_type == "img":
        return f".//img[@src='{element.get_attribute('src')}']"
    elif element_type == "input":
        return f".//input[@type='submit' or @value='Download']"
    elif element_type == "image link":
        return f".//a[@href='{element.get_attribute('href')}']"
    return None

def get_elements_by_type(driver, element_type):
    # Helper function to get elements based on type
    if element_type == "button":
        return get_download_buttons(driver)
    elif element_type == "img":
        return get_img_elements(driver)
    elif element_type == "image link":
        return get_image_links(driver)
    elif element_type == "input":
        return get_download_inputs(driver)
    # elif element_type == "dropdown":
    #     return get_dropdown_download_buttons(driver)
    # elif element_type == "link":
    #     return get_all_download_links(driver)
    return []

# get body elements
def get_body_element(website, driver):
    # Navigate to the website
    driver.get(website)
   
    # Find the <body> element and return it
    body_element = driver.find_element(By.TAG_NAME, 'body')

     # Get the 'id' attribute of the <body> tag (if it exists)
    body_id = body_element.get_attribute('id')
    
    # Print or return the body ID
    print("Body ID:", body_id)
    
    return body_element

# gather image links
def gather_image_links(driver,body_element):
   
    # Gather href links from <a> tags around each <img> element
    # Get the current page URL
    current_page_url = driver.current_url
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

# get download buttons
def get_download_buttons(driver):
    all_buttons = driver.find_elements(By.TAG_NAME, 'button')
    print(f'Length of all_buttons: {len(all_buttons)}')
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

# get img elements
def get_image_links(driver):
    # Locate <a> tags that contain <img> elements, either directly or nested within other elements.
    image_links = [
        a for a in driver.find_elements(By.TAG_NAME, 'a')
        if a.get_attribute('href') and a.find_elements(By.XPATH, ".//img")
    ]
    
    print(f"Found {len(image_links)} potential image link(s) with href.")
    return image_links

# get input download
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

# get img elements
def get_img_elements(driver):
    img_elements = [
        img for img in driver.find_elements(By.TAG_NAME, 'img')
        if img.find_elements(By.XPATH, "ancestor::a[@href]")
    ]
    print(f"Found {len(img_elements)} <img> elements linked to <a> tags with href attributes.")
    return img_elements


def is_new_file_downloaded(download_dir, before_files):
    """Checks for new files in download_dir not present in before_files."""
    # Allow some time for download to initialize
    time.sleep(2)   
    # Get the current list of files in the directory
    after_files = set(os.listdir(download_dir))
    new_files = after_files - before_files  # Files in 'after' but not in 'before'   
    if new_files:
        print("New download detected:", new_files)
        return True
    else:
        print("No new download detected.")
        return False

# Set download directory path here at the start of the script
download_dir = "C:\\Users\\Lenovo\\Downloads"
download_triggered = False  # Flag to track if download started

# Attempt download from each element list
def attempt_download_from_elements(driver, elements, element_type):
    for idx, element in enumerate(elements, start=1):
        try:
            before_files = set(os.listdir(download_dir))
            # Retrieve a unique XPath for each element type
            element_xpath = get_xpath_for_element(element, element_type)
            if not element_xpath:
                print(f"Skipping {element_type} {idx} - Unable to determine XPath.")
                continue            
            # Wait until the element is clickable using the XPath
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
            print(f"{element_type.capitalize()} {idx} is clickable.")

            # Scroll into view and click
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(20)
            driver.execute_script("arguments[0].click();", element)
            print(f"Clicked {element_type} {idx}. Download triggered.")
            time.sleep(200)
            if is_new_file_downloaded(download_dir, before_files):
                return True  # Download successfully triggered
            else:
                return False  # Download not detected
        except Exception as e:
            print(f"Error triggering download with {element_type} {idx}: {e}")
            return False  # If there's an error, stop further iteration for this element type
    return False  # No download triggered in this set of elements


def saveCookies(wd):
    
    cookies = wd.get_cookies()  # Fetch cookies after login
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print("Cookies saved successfully.")


def divide_into_chunks(href_links, num_chunks):
    """Divide href_links into `num_chunks` parts."""
    chunk_size = math.ceil(len(href_links) / num_chunks)
    return [href_links[i:i + chunk_size] for i in range(0, len(href_links), chunk_size)]


def process_links_sequentially(driver, href_links, download_dir, num_chunks=5):
    """Divide href_links into chunks and process them sequentially."""
    chunks = divide_into_chunks(href_links, num_chunks)
    print(f"Divided href_links into {len(chunks)} chunks.")

    for idx, chunk in enumerate(chunks, start=1):
        print(f"Processing chunk {idx}/{len(chunks)} with {len(chunk)} links...")
        search_and_click_thread_download(driver, chunk, download_dir)
        print(f"Completed processing chunk {idx}/{len(chunks)}.")

