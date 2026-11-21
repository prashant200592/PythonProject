# Install pytest-xdist
# pytest -v -s 
import time
import pytest
class TestParallel:
    def test_chromeLogin(self):
        from selenium import webdriver
        # from selenium.webdriver.chrome.service import Service
        # self.service_obj = Service("D:\Installations\Drivers\chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.service_obj)
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.close()


    def test_edgeLogin(self):
        from selenium import webdriver
        # from selenium.webdriver.edge.service import Service
        # self.service_obj = Service("D:\Installations\Drivers\msedgedriver.exe")
        # self.driver = webdriver.Edge(service=self.service_obj)
        self.driver = webdriver.Edge()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.close()

    def test_firefoxLogin(self):
        from selenium import webdriver
        # from selenium.webdriver.firefox.service import Service
        # self.service_obj = Service("D:\Installations\Drivers\geckodriver.exe")
        # self.driver = webdriver.Firefox(service=self.service_obj)
        self.driver = webdriver.Firefox()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.close()
