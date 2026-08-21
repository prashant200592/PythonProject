from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

print("Page title is: ",driver.title)
# driver.find_element(By.XPATH, '//*[@id="search-box"]/span/input').send_keys("products")
# driver.find_element(By.XPATH, '/*[@id="user-selection"]/h5').click()

elements = driver.find_elements(By.CLASS_NAME,"float-left")
print(elements)
print(len(elements))

links = driver.find_elements(By.TAG_NAME,"a")
print(links)
print(len(links))

driver.find_element(By.LINK_TEXT, "Online training for developers").click()
driver.implicitly_wait(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "solution").click()
print(driver.title)


driver.close()



