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
import threading
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


# options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-blink-features=AutomationControlled')

# # Use Service to set the executable path for the WebDriver
# service = Service("./chromedriver/chromedriver.exe")  # Set the correct path to chromedriver here
# driver = webdriver.Chrome(service=service, options=options)


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

def setup_driver(download_dir=None):
    """Initialize the WebDriver."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Use Service to set the executable path for the WebDriver
    service = Service("./chromedriver/chromedriver.exe")  # Set the correct path to chromedriver here
    driver = webdriver.Chrome(service=service, options=options)

    return driver


# # Example usage
driver = setup_driver()

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
                divide_and_process(driver, href_links)
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


def load_cookies_and_login(driver, cookies, url="https://modelo.io/"):
    """Load cookies into the driver, validate session login, and navigate to a specific page."""
    # Open the base URL
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    
    # Add cookies
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()  # Refresh to apply cookies
    time.sleep(2)  # Wait for the session to stabilize
    
    # Navigate to the specific URL
    driver.get("https://www.modelo.io/damf/myspace?locale=en_US")
    time.sleep(2)  # Allow the page to load
    
    try:
        # Locate the title content (customize the selector as needed)
        title_element = driver.find_element(By.TAG_NAME, "title")  # Adjust selector based on the actual element
        print(f"Page title: {title_element.get_attribute('innerText')}")
        print("Login successful!")
        return True
    except Exception as e:
        print(f"Error locating title: {e}")
        print("Login failed. Please check the cookies or page structure.")
        return False

def search_and_click_download_button(driver, href_links):
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
                if attempt_download_from_elements(driver, elements, successful_element_type):
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
                if attempt_download_from_elements(driver, elements, element_type):
                    print(f"Download triggered by {element_type}.")            
                    successful_element_type = element_type  # Save the successful element type
                    break  # Exit element checks since download was triggered

        except TimeoutException:
            print("Timeout waiting for page load.")
        except Exception as e:
            print(f"An error occurred while processing {link}: {e}")

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
                if attempt_download_from_elements(driver, elements, successful_element_type):
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
                if attempt_download_from_elements(driver, elements, element_type):
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


cookies = [{"domain": ".modelo.io", "httpOnly": False, "name": "ModeloUtmInfoV2", "path": "/", "sameSite": "Lax", "secure": False , "value": "{%22utm_source%22:%22None%22%2C%22utm_campaign%22:%22None%22%2C%22utm_medium%22:%22%22%2C%22utm_term%22:%22%22%2C%22utm_content%22:%22%22}"}, {"domain": ".modelo.io", "expiry": 1766690349, "httpOnly": False, "name": "_ga", "path": "/", "sameSite": "Lax", "secure": False, "value": "GA1.1.775094576.1732130334"}, {"domain": ".modelo.io", "expiry": 1739906328, "httpOnly": False, "name": "_gcl_au", "path": "/", "sameSite": "Lax", "secure": False, "value": "1.1.1094416631.1732130328.1330021933.1732130339.1732130338"}, {"domain": ".modelo.io", "expiry": 1763666351, "httpOnly": False, "name": "mp_d5b1134c52f7ef61826c4f1f22f5f996_mixpanel", "path": "/", "sameSite": "Lax", "secure": False, "value": "%7B%22distinct_id%22%3A%20%22%24device%3A1934b034c321226-03870543dd6717-31251943-100200-1934b034c321227%22%2C%22%24device_id%22%3A%20%221934b034c321226-03870543dd6717-31251943-100200-1934b034c321227%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D"}, {"domain": ".modelo.io", "expiry": 1766690349, "httpOnly": False, "name": "_ga_N7JMBXMDFL", "path": "/", "sameSite": "Lax", "secure": False, "value": "GS1.1.1732130336.1.1.1732130349.47.0.0"}, {"domain": ".modelo.io", "httpOnly": False, "name": "qh-locale", "path": "/", "sameSite": "Lax", "secure": False, "value": "en_US"}, {"domain": ".modelo.io", "expiry": 1732216749, "httpOnly": False, "name": "_gid", "path": "/", "sameSite": "Lax", "secure": False, "value": "GA1.2.1637627430.1732130334"}, {"domain": ".modelo.io", "expiry": 1732130394, "httpOnly": False, "name": "_gat_UA-50607635-1", "path": "/", "sameSite": "Lax", "secure": False, "value": "1"}, {"domain": ".modelo.io", "expiry": 1766690324, "httpOnly": False, "name": "qhdi", "path": "/", "sameSite": "Lax", "secure": False, "value": "427eb6a5a77411ef9c40378911bf6857"}]


def process_links(driver, href_links, thread_id):
    """
    Process a portion of href links to search and attempt downloads.

    Args:
        driver: Shared Selenium WebDriver instance.
        href_links: List of href links assigned to this thread.
        thread_id: Identifier for the thread.
    """
    print(f"Thread-{thread_id}: Starting with {len(href_links)} links.")
    successful_element_type = None
    
    if not load_cookies_and_login(driver, cookies):
        print(f"Thread-{thread_id}: Login failed, cannot process links.")
        return

    for link in href_links:
        try:
            driver.get(link)
            print(f"Thread-{thread_id}: Navigated to {link}")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            # Add your download logic here
            if successful_element_type:
                elements = get_elements_by_type(driver, successful_element_type)
                if attempt_download_from_elements(driver, elements, successful_element_type):
                    print(f"Thread-{thread_id}: Download triggered using {successful_element_type}.")
                    continue

            element_checks = [
                ("button", get_download_buttons(driver)),
                ("img", get_img_elements(driver)),
                ("image link", get_image_links(driver)),
                ("input", get_download_inputs(driver)),
            ]

            for element_type, elements in element_checks:
                print(f"Thread-{thread_id}: Attempting {element_type} download.")
                if attempt_download_from_elements(driver, elements, element_type):
                    print(f"Thread-{thread_id}: Download triggered by {element_type}.")
                    successful_element_type = element_type
                    break

        except Exception as e:
            print(f"Thread-{thread_id}: Error processing {link}: {e}")

    print(f"Thread-{thread_id}: Completed.")

def divide_and_process(driver, href_links):
    """
    Divide href links into three parts and process them using threads.

    Args:
        driver: Shared Selenium WebDriver instance.
        href_links: List of all href links to process.
    """
    # Divide the href_links into three portions
    num_threads = 3
    portions = [href_links[i::num_threads] for i in range(num_threads)]

    # Create and start threads
    threads = []
    for i, portion in enumerate(portions):
        thread = threading.Thread(target=process_links, args=(driver, portion, i + 1))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads have completed.")



