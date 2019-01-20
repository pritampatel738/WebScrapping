from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
#driver.maximize_window()
driver.get("http://www.fb.com")

driver.find_element_by_xpath("//input[@id='email']").send_keys("pritam")
driver.find_element_by_xpath("//input[@id='pass']").send_keys("patel")
driver.find_element_by_name("firstname").send_keys("Pritam")
driver.find_element_by_name("lastname").send_keys("Patel")
driver.find_element_by_name("reg_email__").send_keys("7979972939")
driver.find_element_by_name("reg_passwd__").send_keys("8563980812p")
#driver.find_element_by_name().send_keys()
print(driver.title)
