from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj=Service("D:\Installations\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://www.screener.in/")
driver.maximize_window()


driver.find_element(By.PARTIAL_LINK_TEXT, "LOGIN").click()

driver.find_element(By.NAME, "username").send_keys("prashant.pansare2092@gmail.com")
driver.find_element(By.NAME, "password").send_keys("cde3$RFV")
driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/form/button').click()

driver.find_element(By.LINK_TEXT, "Persistent Systems Ltd").click()

driver.find_element(By.XPATH, "/html/body/div/div[2]/div/a[7]").click()

driver.find_element(By.XPATH,'//*[@id="balance-sheet"]/div[1]/div[2]/button').click()

driver.implicitly_wait(5)

#Check Buy Back
driver.find_element(By.CSS_SELECTOR, "button[data-tab-id=corporate-actions-buyback]").click()
driver.implicitly_wait(5)

#Check bonus
#driver.find_element(By.XPATH, '//button[@data-tab-id="corporate-actions-bonus" or @class="active"]').click()
#driver.find_element(By.XPATH, '//*[@id="modal-e62d004cda368"]/div/div[2]/div[1]/div/button[4]').click()
#driver.find_element(By.XPATH, "//button[starts-with(@data-tab-id,'corporate') and contains(@data-tab-id,'bonus')]").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Bonus']").click()
driver.find_element(By.XPATH, "//i[@class='icon-cancel-thin font-size-18 ink-700']").click()


#Get insider traders data
driver.find_element(By.XPATH, "//a[text()='Investors']").click()
driver.implicitly_wait(5)
#driver.find_element(By.CSS_SELECTOR, "button[class=button-secondary button-small]").click
driver.find_element(By.XPATH, '//button[@class="button-secondary button-small"]').click()
driver.find_element(By.XPATH, '//*[@id="trades-insider-trades"]/div/div/label/input').click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//i[@class="icon-cancel-thin font-size-18 ink-700"]').click()



#driver.close()


