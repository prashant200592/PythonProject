import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wikisearch = driver.find_element(By.CSS_SELECTOR, "input#Wikipedia1_wikipedia-search-input")
wikisearch.send_keys("selenium")
wikisearch.submit()

searchlinks = driver.find_elements(By.XPATH, "//a[contains(text(),'Selenium') and @target='_blank']")
print(len(searchlinks))

for searchlink in searchlinks:
    searchlink.click()

wins = driver.window_handles
print(wins)

for win in wins:
    driver.switch_to.window(win)
    time.sleep(1)
    print(driver.title)


time.sleep(2)


for win in wins:
    driver.switch_to.window(win)
    if driver.title == 'Selenium disulfide - Wikipedia':
        driver.close()


print("Success!!!")
time.sleep(300)


