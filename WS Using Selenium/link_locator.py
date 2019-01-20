from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
#driver.maximize_window()
driver.get("http://www.fb.com")
driver.find_element_by_link_text("Log In").click()
driver.back()
time.sleep(4)
driver.find_element_by_partial_link_text("Forgotten").click()
print(driver.title)
