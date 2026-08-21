from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/index.html")
driver.maximize_window()

driver.find_element(By.XPATH, '//a[text()="Market News"]').click()