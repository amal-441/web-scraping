from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from django.conf import settings
import json
import time
import os


def login_and_save_cookies(wd,login_url,dashboard_url):
    # Extract login_url and dashboard_url from the request data
    # login_url = request.data.get('login_url')
    # dashboard_url = request.data.get('dashboard_url')

    # # Validate if the required fields are provided
    # if not login_url or not dashboard_url:
    #     return JsonResponse({'error': 'login_url and dashboard_url are required.'}, status=400)
    
   
    try:
        
        print('wd WebDriverManager initialized!')

        # # Step 1: Go to login URL
        wd.get(login_url)
        print("Go to the Url:")

        # Wait for the page to load
        try:
            WebDriverWait(wd, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("Page fully loaded!")
        except Exception as e:
            print(f"Page not loaded within time: {e}")
            return JsonResponse({'error': 'Failed to load login page.'}, status=500)

        # Get all form elements on the page
        form_elements = wd.find_elements(By.TAG_NAME, "form")
        print(f"{len(form_elements)} form(s) found!")

        for form_element in form_elements:
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

                # Add password input XPath search without changing the existing code.
                password_input = form_element.find_element(
    By.XPATH,
    "//input[" 
    "contains(translate(@id, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'password') or "
    "contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'password') or "
    "@type='password' or "
    "contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'password') or "
    "(@id='password' or @type='password' or @name='password') or "
    "contains(@class, 'StyledInput') or "
    "contains(@class, 'muya-input-input')"
    "]"
)
                password_input.send_keys("model.io123")  # Replace with your actual password
                print("Password Entered")

                submit_button = form_element.find_element(By.XPATH, "//*[contains(@type, 'submit') or contains(@value, 'Login') or contains(@value, 'Sign In')]")
                submit_button.click()
                print("Login form submitted.")

                # Step 4: Verify successful login by navigating to the dashboard
                # WebDriverWait(wd, 10).until(
                #     EC.presence_of_element_located((By.TAG_NAME, "body"))
                # )
                # If we reached the dashboard, login was successful
                print("Login successful!")
                time.sleep(10)
                # Save cookies to cookies.json
                # Wait for the dashboard to load to verify successful login
                # Save cookies after successful login
                 # Save cookies to the root directory
                # After logging in, save cookies to project root directory
                saveCookies(wd)
                
                wd.get(dashboard_url)  # Navigate to the dashboard page
                
                print("Dashboard loaded. Login successful!")
                print("Login confirmed and dashboard is accessible!")

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
            except Exception as e:
                print(f"Error interacting with the form: {e}")
                continue  # Try the next form if the current one fails
        return JsonResponse({'error': 'Failed to log in. No suitable form found.'}, status=400)

    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'error': str(e)}, status=500)

# Function to save cookies to a file
def saveCookies(wd):
    
    cookies = wd.get_cookies()  # Fetch cookies after login
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print("Cookies saved successfully.")


class WebDriverUtils:
    def __init__(self, driver):
        self.driver = driver

    def get_cookies(self):
        """
        Retrieve cookies from Selenium WebDriver.
        :return: Dictionary of cookies
        """
        cookies = {}
        selenium_cookies = self.driver.get_cookies()
        for cookie in selenium_cookies:
            cookies[cookie['name']] = cookie['value']
        return cookies

    def dump_cookies(self, output_file_path):
        """
        Save cookies to a JSON file.
        :param output_file_path: Path to save cookies.
        """
        cookies = self.get_cookies()
        with open(output_file_path, 'w') as f:
            json.dump(cookies, f)
        print(f"Saved cookies to: {output_file_path}")



def load_cookies(wd, path):
    """
    Loads cookies from a JSON file and adds them to the WebDriver session.
    :param wd: WebDriver instance
    :param path: Path to the cookies file
    """
    try:
        with open(path, 'r') as f:
            cookies = json.load(f)
        
        # Iterate through the cookies and add each one to the WebDriver
        for name, value in cookies.items():
            wd.add_cookie({
                'name': name,
                'value': value,
                'path': '/',  # Default path for cookies
                'domain': None  # No domain specified
            })
        
        print(f"Cookies loaded from: {path}")
    except Exception as e:
        print(f"Error loading cookies from {path}: {e}")