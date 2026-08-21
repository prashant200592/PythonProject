from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

ele=driver.find_element(By.XPATH, "//input[@id='field1']")

act=ActionChains(driver)
act.double_click(ele).perform()

dcbutton=driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act.double_click(dcbutton).perform()

print("Success!!!")