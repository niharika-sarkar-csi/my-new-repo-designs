from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open GitHub login page
driver.get("https://github.com/login")

# Enter username
driver.find_element(By.ID, "login_field").send_keys("niharika.sarkar@cloudspikes.ca")

# Enter password
driver.find_element(By.ID, "password").send_keys("000999@@Niharika")

# Click the login button
driver.find_element(By.NAME, "commit").click()

time.sleep(3)
driver.quit()

