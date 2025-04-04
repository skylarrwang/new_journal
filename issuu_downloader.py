from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver (Update if needed)
CHROMEDRIVER_PATH = "./chromedriver"

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": "./downloads",  # Your download folder
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options.add_argument("--start-maximized")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# --- LOGIN ---
driver.get("https://issuu.com/login")
wait.until(EC.presence_of_element_located((By.NAME, "email")))

email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")
email.send_keys("thenewjournalatyale@gmail.com")
password.send_keys("305crown")
password.send_keys(Keys.RETURN)

# --- NAVIGATE TO PUBLICATIONS PAGE ---
wait.until(EC.url_contains("home"))
driver.get("https://issuu.com/home/published")
time.sleep(5)

# --- LOAD ALL PUBLICATIONS ---
while True:
    try:
        load_more_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(text(), "Load more")]')))
        print("Clicking 'Load more'...")
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
        load_more_button.click()
        time.sleep(10)  # Wait for new content to load
    except:
        print("No more 'Load more' buttons or timed out.")
        break

time.sleep(5)

# --- GET ALL PUBLICATION MENUS ---
menu_buttons = driver.find_elements(By.XPATH, '//svg[contains(@xlink:href, "#icon-more")]/ancestor::button')
print(f"Found {len(menu_buttons)} publication menus.")

for index, menu_button in enumerate(menu_buttons):
    try:
        print(f"Opening menu for publication #{index + 1}")
        driver.execute_script("arguments[0].scrollIntoView();", menu_button)
        menu_button.click()

        # Wait for the dropdown and click "Download Publication"
        download_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(text(), "Download Publication")]')))
        download_option.click()
        print(f"Clicked 'Download Publication' for issue #{index + 1}")

        time.sleep(10)  # Wait for download to begin
    except Exception as e:
        print(f"Failed to download issue #{index + 1}: {e}")
        continue

print("All downloads attempted.")
driver.quit()
