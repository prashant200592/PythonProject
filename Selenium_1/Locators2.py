from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

images = driver.find_elements(By.CLASS_NAME, "item-img")
print("images: ",len(images))

links = driver.find_elements(By.TAG_NAME, "a")
print("Links: ",len(links))


driver.close()