import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj )

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[text()='Prompt']").click()

alertwindow = driver.switch_to.alert

# Print alert message text
print(alertwindow.text)
time.sleep(3)

# Enter text in alert message 
alertwindow.send_keys("Prashant")

# Accept alert message
alertwindow.accept()
time.sleep(3)

# Dismiss alert message
# alertwindow.dismiss()

driver.find_element(By.XPATH, "//button[text()='Alert']").click()

# Accept alert message
driver.switch_to.alert.accept()
time.sleep(2)


driver.find_element(By.XPATH, "//button[text()='Confirm Box']").click()
driver.switch_to.alert.accept()