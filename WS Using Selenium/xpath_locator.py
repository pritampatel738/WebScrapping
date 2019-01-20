from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
#driver.maximize_window()
driver.get("http://www.fb.com")

driver.find_element_by_xpath("//input[@id='email']").send_keys("pritam")
driver.find_element_by_xpath("//input[@id='pass']").send_keys("patel")
print(driver.title)
