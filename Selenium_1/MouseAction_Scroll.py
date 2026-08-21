from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time

service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# # Approach 1:
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels vertically moved: ", value)

# # Approach 2:
# indflag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", indflag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Pixels vertically moved: ", value)

# Approach 3:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Height of vertical scroll bar is: ", value)

time.sleep(5)

# Scroll up to starting position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
value1 = driver.execute_script("return window.pageYOffset;")
print("Scrollbar starts at: ", value1)


print("Success!!!")