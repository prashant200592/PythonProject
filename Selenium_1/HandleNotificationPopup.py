#ops = webdriver.ChromeOptions() >> ops.add_argument("--disable-notifications")

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=ops)
driver.implicitly_wait(10)

driver.get("https://whatmylocation.com/")
driver.maximize_window()




print("Success!!!")
time.sleep(300)

