from selenium.webdriver.common.by import By

# to get body elements of the webpage
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