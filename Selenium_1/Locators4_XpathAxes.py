from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service("D:\Installations\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=service_object)

driver.get("https://money.rediff.com/index.html")
driver.maximize_window()

driver.find_element(By.XPATH, '//a[text()="Gainers / Losers"]').click()
# driver.find_element(By.XPATH, "//a[text()='Market News']").click()
# driver.find_element(By.XPATH, '//a[text()="Trends"]').click()
# driver.find_element(By.XPATH, "(//a[normalize-space()='Airan Ltd.'])[1]").click()
# driver.find_element(By.XPATH, '//a[text()="Balance Sheet"]').click()

# #ISF Ltd.
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'ISF Ltd.')]/self::a").text
# print(text_msg)

#driver.find_element(By.XPATH, "//a[contains(text(), 'ISF Ltd.')]/self::a").click()

#driver.close()