#driver.switch_to.frame(name/id/webelement/index-0)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_object = Service("D:\Installations\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service = service_object)
driver.implicitly_wait(10)

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# driver.switch_to.frame("frame-one796456169")
# driver.find_element(By.CSS_SELECTOR, "input#RESULT_TextField-0").send_keys("Prashant")
#
# driver.switch_to.default_content()


driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

# Switch to outer frame through frame element
outerframe = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
driver.switch_to.frame(outerframe)

# Switch to inner frame through frame element
innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Prashant")

# Switch to parent frame
driver.switch_to.parent_frame()

driver.switch_to.default_content()


print("Success...")
