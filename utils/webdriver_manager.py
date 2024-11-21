from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from django.conf import settings

class WebDriverManager:
    _driver_instance = None

    @staticmethod
    def get_driver():
        """Get or create a shared WebDriver instance."""
        if WebDriverManager._driver_instance is None:
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            # Uncomment for headless mode
            # options.add_argument('--headless')

            chromedriver_path = os.path.join(settings.BASE_DIR, "chromedriver", "chromedriver.exe")
            service = Service(chromedriver_path)
            WebDriverManager._driver_instance = webdriver.Chrome(service=service, options=options)
        return WebDriverManager._driver_instance

    @staticmethod
    def quit_driver():
        """Quit the shared WebDriver instance."""
        if WebDriverManager._driver_instance is not None:
            WebDriverManager._driver_instance.quit()
            WebDriverManager._driver_instance = None
