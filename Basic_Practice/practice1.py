from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

service_obj=Service("D:\Installations\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj, options=ops)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
#driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()


# dateframe=driver.find_element(By.XPATH, '//*[@id="content"]/iframe')
# driver.switch_to.frame(dateframe)

date=driver.find_element(By.XPATH, '//*[@id="datepicker"]')
date.send_keys("11/03/23")


print("Success!!!")
