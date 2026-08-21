from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("D:\Installations\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

rightclickbutton=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)
act.context_click(rightclickbutton).perform()

driver.find_element(By.XPATH, "/html/body/ul/li[1]/span").click()

driver.switch_to.alert.accept()

print("Success!!!")

