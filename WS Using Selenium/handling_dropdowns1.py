from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://airindia.in")

driver.find_element_by_xpath("//input[@id='from']").send_keys("ban")
time.sleep(5)
driver.find_element_by_partial_link_text("Thailand").click()
driver.find_element_by_name("to").send_keys("Del")
time.sleep(5)
driver.find_element_by_partial_link_text("Indira Gandhi").click()