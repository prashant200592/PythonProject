from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

service_obj=Service("D:\Installations\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj, options=ops)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# # Approach 1:
# dateframe=driver.find_element(By.XPATH, '//*[@id="content"]/iframe')
# driver.switch_to.frame(dateframe)
#
# datepicker=driver.find_element(By.XPATH, "//input[@id='datepicker']")
# datepicker.click()
# datepicker.send_keys("19/11/2023")

# Approach 2:
dateframe = driver.find_element(By.XPATH, '//*[@id="content"]/iframe')
driver.switch_to.frame(dateframe)
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()


year="2022"
month="May"
date="20"

while True:

    yr=driver.find_element(By.XPATH, '//span[@class="ui-datepicker-year"]').text
    mon=driver.find_element(By.XPATH, '//span[@class="ui-datepicker-month"]').text

    if yr==year and mon==month:
        break
    else:
        driver.find_element(By.XPATH, '//span[@class="ui-icon ui-icon-circle-triangle-w"]').click()

dates=driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')

for d in dates:
    if d.text==date:
        d.click()
        break




print("Success!!!")