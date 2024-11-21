import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from django.conf import settings

class WebDriverManager:
    _instance = None

    def __init__(self):
        if WebDriverManager._instance is not None:
            raise Exception("This class is a singleton!")
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')

        # Use Service to set the executable path for the WebDriver
        chromedriver_path = os.path.join(settings.BASE_DIR, "chromedriver", "chromedriver.exe")
        service = Service(chromedriver_path)
        print("service configured")

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=service, options=options)

    @staticmethod
    def get_instance():
        if WebDriverManager._instance is None:
            WebDriverManager._instance = WebDriverManager()
        return WebDriverManager._instance

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            WebDriverManager._instance = None
