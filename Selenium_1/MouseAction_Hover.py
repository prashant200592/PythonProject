from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service_obj=Service("D:\Installations\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj)


# Hover
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

helpicon=driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-question-lg']")

act=ActionChains(driver)

act.move_to_element(helpicon).click().perform()





print("Success!!!")

