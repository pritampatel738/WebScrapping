from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://www.google.com")

driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("google")

print(driver.title)
time.sleep(5)
driver.quit()