from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

def dynamic_scraper_function(target_url):
    try:
        # Setting up Chrome options for headless browsing
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

        # Path to chromedriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(target_url)
        time.sleep(2)  # Wait for the page to load

        # Initialize a list to store multiple records
        scraped_data = []

        # Keywords for dynamic scraping
        keywords = {
            'camp_name': ['camp name', 'camp_title', 'name of camp', 'camp_name', 'jet-listing-dynamic-field__content'],
            'address': ['address', 'location', 'camp address', 'camp_location'],
            'activities': ['activities', 'programs', 'offerings', 'camp activities'],
            'cost': ['cost', 'price', 'fee', 'tuition'],
            'date': ['date', 'schedule', 'duration', 'camp schedule'],
        }

        # Define a list of possible class names (these could be different for different sections)
        possible_class_names = [
           
            "jet-listing-grid__items"
            # Add more potential class names here if needed
        ]

        # Initialize an empty list to store all matching sections
        all_sections = []

        # Iterate over possible class names and collect all matching sections
        for class_name in possible_class_names:
            sections = driver.find_elements(By.CLASS_NAME, class_name)
            all_sections.extend(sections)  # Add found sections to the list

        if not all_sections:
            print("No sections found, check your CSS selectors.")

        # Scrape data from each of the found sections
        for section in all_sections:
            print("Scraping new section...")
            # Initialize a dictionary for each section of data (each camp)
            data = {}

            # Try to find each keyword in the section using multiple selectors
            for key, possible_labels in keywords.items():
                for label in possible_labels:
                    try:
                        print(f"Searching for label: {label}")

                        # Look for the text content of the element based on the label keywords
                        value = None

                        # Try to find the value in the section based on the label
                        if label.lower() in section.text.lower():
                            value = section.text.strip()

                        if value:
                            print(f"Found {key}: {value}")
                            data[key] = value
                            break  # Stop searching for more labels for this key

                    except Exception as e:
                        print(f"Error finding label {label}: {str(e)}")
                        continue  # Continue to the next label if one fails

            # If no data was found for key fields, assign a fallback value
            for key in keywords.keys():
                if key not in data:
                    data[key] = f"{key.replace('_', ' ').title()} Not Found"
            
            # If any data was found, append it to the scraped_data list
            if data:
                print(f"Appending data: {data}")
                scraped_data.append(data)

        print(f"Scraped Data: {scraped_data}")

        return {'status': 'success', 'data': scraped_data}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {'status': 'error', 'message': str(e)}

    finally:
        driver.quit()
