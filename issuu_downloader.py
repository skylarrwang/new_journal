from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to ChromeDriver (Update this path!)
CHROMEDRIVER_PATH = "./chromedriver"

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": "./downloads",  # Change to your preferred folder
    "download.prompt_for_download": False,
})

from selenium.webdriver.chrome.service import Service

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Open Issuu login page
driver.get("https://issuu.com/login")
time.sleep(3)

# Login (Replace with your credentials)
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")
email.send_keys("thenewjournalatyale@gmail.com")
password.send_keys("305crown")
password.send_keys(Keys.RETURN)
time.sleep(5)

# Navigate to "My Publications"
driver.get("https://issuu.com/home/published")
time.sleep(5)

# Find download links and click them
downloads = driver.find_elements(By.XPATH, '//a[contains(@href, "/download")]')
for dl in downloads:
    dl.click()
    time.sleep(5)  # Wait for download

print("Downloads complete.")
driver.quit()
