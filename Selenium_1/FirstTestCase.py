
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)

#driver.find_element_by_name("username").send_keys("Admin")
driver.find_element(By.NAME, "username").send_keys("Admin")

#driver.find_element_by_name("password").send_keys("admin123")
driver.find_element(By.NAME, "password").send_keys("admin123")

#driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login test passed...")
else:
    print("Login test failed...")

driver.close()

print("Program completed... Work on another program now :)")
