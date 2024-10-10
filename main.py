import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Load environment variables from the .env file
load_dotenv()

# Fetch credentials and settings from environment variables
EMAIL = os.getenv("EMAIL")  # Your email address for login
USERNAME = os.getenv("USERNAME")  # Your username for login
PWD = os.getenv("PASSWORD")  # Your password for login
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")  # Path to your ChromeDriver executable
PROMISED_DOWN = 150  # Expected download speed (in Mbps)
PROMISED_UP = 10  # Expected upload speed (in Mbps)

# Configure Chrome WebDriver with service and options
service = Service(executable_path=CHROME_DRIVER_PATH)
options = Options()
options.add_experimental_option("detach", True)  # Keep browser window open after execution
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()  # Maximize the browser window

# Class to handle internet speed test and Twitter interaction
class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.up = 0  # Upload speed placeholder
        self.down = 0  # Download speed placeholder

    # Method to get internet speed from speedtest.net
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")  # Navigate to Speedtest website
        time.sleep(1)  # Wait for the page to load
        self.driver.fi


