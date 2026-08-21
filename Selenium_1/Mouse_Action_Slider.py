from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
from selenium.webdriver import ActionChains

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

act = ActionChains(driver)

sliderleft = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default' and @style='left: 0%;']")

print(sliderleft.location)

act.drag_and_drop_by_offset(sliderleft, 100, 0).perform()

print(sliderleft.location)


print("Success!!!")