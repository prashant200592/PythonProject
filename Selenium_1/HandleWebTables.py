# WebTables: Static and Dynamic

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

service_obj=Service("D:\Installations\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj, options=ops)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# Count #tr and #td
noTableRows=driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print("Number of rows: ", len(noTableRows))

# Count #th
noTableColumns=driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th")
print("No of columns: ", len(noTableColumns))

# Read specific row and column data

specificData=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]")
print("Specific data: ", specificData.text)

# Read all the table data
# tableDatas = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[*]/td[*]") # Not working
# for tableData in tableDatas:
#     print(tableData.text)


for r in range(2, len(noTableRows)+1):
    for c in range(1, len(noTableColumns)+1):
        tableData=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]")
        print(tableData.text, end='     ')
    print()

# Print queried data e.g. Print book name where author is Mukesh


rows=driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
print("Rows: ", len(rows))

columns=driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th")
print("Columns: ", len(columns))

# for rw in range(2, len(rows)+1):
#     for cl in range(1, len(columns)+1):
#         data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rw)+"]/td["+str(cl)+"]")
#         print(data.text, end="  ")
#     print()

# My Logic
for rw in range(2, len(rows)+1):
    for cl in range(1, len(columns)+1):
        data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rw)+"]/td["+str(cl)+"]")
        if data.text == 'Mukesh':
            print("Book written by Mukesh: ", driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rw)+"]/td["+str(cl-1)+"]").text)
            #3,2    5,2

# Trainers Logic

for r in range(2, len(rows)+1):
    authorName=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == 'Mukesh':
        price=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print("Book witten by Mukesh Sir: ", driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text, "  ", price)


print("Success!!!")
