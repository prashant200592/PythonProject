# driver.switch_to.window(window_ID)
# driver.current_window_handle >> current window handle >> window ID of single browser window
# driver.window_handles >> Return window IDs of multiple browser windows
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

windowhandle = driver.current_window_handle
print("Current window ID is: ", windowhandle)
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='New Browser Window']").click()


# driver.close() # Closes first focussed browser window

windowhandles = driver.window_handles
print("Window handles are: ", driver.window_handles)


driver.switch_to.window(windowhandles[1])
time.sleep(2)
print("Title of child window: ", driver.title)

driver.switch_to.window(windowhandles[0])
print("Title of parent window: ", driver.title)


wins = driver.window_handles

for win in wins:
    driver.switch_to.window(win)
    print(driver.title)

time.sleep(2)

for win in wins:
    driver.switch_to.window(win)
    if driver.title == 'Your Store':
        driver.close()

time.sleep(2)

# print("Remaining page: ", driver.title)


# driver.close()

print("Success!!!")