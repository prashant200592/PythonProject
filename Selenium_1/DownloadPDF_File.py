from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

    preferences = {"download.default_directory": location,
                   "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    ops.add_argument("--disable-notifications")

    my_driver = webdriver.Chrome(service=service_obj, options=ops)
    my_driver.implicitly_wait(10)

    return my_driver


driver = chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

print("Success!!!")
time.sleep(300)