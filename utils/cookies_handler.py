from django.http import JsonResponse
from utils.cookies_handler import WebDriverHelper
import os

def login_and_save_cookies(request):
    driver_path = os.path.join("chromedriver", "chromedriver.exe")
    cookies_file_path = os.path.join(os.getcwd(), "cookies.pkl")
    login_url = "https://app.modelo.io/login"
    email = "amaldq333@gmail.com"  # Replace with actual email
    password = "model.io123"  # Replace with actual password

    try:
        helper = WebDriverHelper(driver_path, cookies_file_path)

        # Attempt to load cookies and refresh the page
        helper.load_cookies()
        helper.driver.refresh()

        # If cookies fail, perform login
        if not helper.login_to_website(login_url, email, password):
            return JsonResponse({'error': 'Login failed. Please check your credentials.'}, status=400)

        # Save cookies after login
        helper.save_cookies()
        helper.close_all_tabs()
        helper.driver.quit()

        return JsonResponse({'message': 'Logged in and cookies saved successfully.'}, status=200)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
