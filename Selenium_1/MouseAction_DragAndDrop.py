from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drag = driver.find_element(By.XPATH, "//p[normalize-space()='Drag me to my target']")
drop = driver.find_element(By.XPATH, "//p[normalize-space()='Drop here']")

act = ActionChains(driver)
act.drag_and_drop(drag,drop).perform()

print("Success!!!")