from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://airindia.in")
time.sleep(15)
driver.find_element_by_xpath("//input[@id='from']").send_keys("ban")
time.sleep(5)
driver.find_element_by_partial_link_text("Thailand").click()
driver.find_element_by_name("to").send_keys("Del")
time.sleep(5)
driver.find_element_by_partial_link_text("Indira Gandhi").click()

dropdown = Select(driver.find_element_by_xpath("//*[@id='_classType1']"))
dropdown.select_by_index(3)
time.sleep(5)
dropdown.select_by_value("Business")