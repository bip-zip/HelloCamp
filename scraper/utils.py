from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def dynamic_scraper_function(target_url):
    # Set up Selenium options
    options = Options()
    options.add_argument("--headless=new")  # Use the latest headless mode
    options.add_argument("--no-sandbox")  # Bypass the sandbox
    options.add_argument("--disable-dev-shm-usage")  # Use shared memory more efficiently

    # Path to ChromeDriver or use a manager (change as needed)
    service = Service("C:/Program Files/Chrome/chromedriver.exe")  # Update with the actual path to your ChromeDriver
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Initialize the WebDriver with service and options
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the target URL
        driver.get(target_url)
        time.sleep(2)  # Wait for the page to load (adjust as needed)

        # Example scraping logic (replace selectors with actual ones from the website)
        camp_name = driver.find_element('id', 'camp_name').text
        address = driver.find_element('id', 'camp_address').text

        # Organize the scraped data into a dictionary
        data = {
            'camp_name': camp_name,
            'address': address
        }

        return {'status': 'success', 'data': data}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}

    finally:
        driver.quit()
