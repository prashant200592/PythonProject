#Application, Conditional, Browser, Navigational, Wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.find_element(By.XPATH, '//a[text()="Register"]').click()





#driver.close()