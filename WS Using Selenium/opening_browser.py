from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
driver.get("http://www.google.com")

driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("google")
