from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
import os
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
prefs = {
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.geolocation": 2
}
ops.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options=ops)

driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()

# Sending data to input box
driver.find_element(By.ID, "name").send_keys("Prashant")
driver.find_element(By.ID, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "phone").send_keys("12345")
driver.find_element(By.ID, "textarea").send_keys("Pune")

# Selecting radio button
driver.find_element(By.ID, "male").click()

# Selecting checkbox
driver.find_element(By.CSS_SELECTOR, "input[id='sunday']").click()

# Selecting drop-down options
country = driver.find_element(By.XPATH, "//select[@id='country']")
country_dropdown = Select(country)
country_dropdown.select_by_visible_text("India")

driver.find_element(By.XPATH, "//option[normalize-space()='Blue']").click()

driver.find_element(By.XPATH, "//option[normalize-space()='Lion']").click()

# Selecting date value - send_keys()
driver.find_element(By.ID, "datepicker").send_keys("11/17/2026")

# Uploading file - send_keys()
driver.find_element(By.ID, "singleFileInput").send_keys("C:\\Users\\Megha Kadam\\Downloads\\GT_Contri.xlsx")

# Handle alert
driver.find_element(By.ID, "promptBtn").click()
alert = driver.switch_to.alert
print("Alert text: ", alert.text)
alert.send_keys("Python-Selenium-PyTest")
alert.accept()

# Handle multiple windows
driver.find_element(By.XPATH, "//button[normalize-space()='New Tab']").click()
current_window = driver.current_window_handle
print("Current window handle: ", current_window)
windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    print("Window title: ", driver.title)
    if driver.title == "SDET-QA Blog":
        driver.close()


# Mouse hover
driver.switch_to.window(current_window)
mywait = WebDriverWait(driver,timeout=10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
point_me = mywait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Point Me']")))
laptops = driver.find_element(By.XPATH, "//a[normalize-space()='Laptops']")
act = ActionChains(driver)
act.move_to_element(point_me).move_to_element(laptops).click().perform()

# Double click
dbclick_ele = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act.double_click(dbclick_ele).perform()

# Keyboard
txtbox = driver.find_element(By.ID, "field2")
txtbox.click()
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
driver.save_screenshot(os.path.join(os.path.abspath(os.pardir),'screenshots','deleted_text.png'))

# Drag and drop
source_ele = driver.find_element(By.XPATH, "//p[text()='Drag me to my target']")
target_ele = driver.find_element(By.ID, "droppable")
act.drag_and_drop(source_ele, target_ele).perform()

# Slider
source_ele = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
print("Location of slider: ", source_ele.location)
act.drag_and_drop_by_offset(source_ele,2000,2112)

# scroll
#driver.execute_script("window.scrollBy(0, 1000);")
driver.execute_script("arguments[0].scrollIntoView(true);", source_ele)

# save screenshot
driver.save_screenshot(os.path.join(os.path.abspath(os.pardir),'screenshots','moved_slider.png'))



time.sleep(10)
driver.quit()
print("Executed form script successfully....")
