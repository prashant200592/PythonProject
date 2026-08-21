import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

    my_driver = webdriver.Chrome(service=service_obj)
    my_driver.implicitly_wait(10)

    return my_driver

driver = chrome_setup()

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()

driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C:/Users/Megha Kadam/OneDrive/Desktop/sample_150kB.pdf")

print("Success!!!")
time.sleep(300)