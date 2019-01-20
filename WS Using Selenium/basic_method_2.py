from selenium import webdriver
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
#driver.maximize_window()
driver.get("http://www.gmail.com")


driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']").send_keys("pritampatel963@gmail.com")
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(10)
driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']").send_keys("8563980812p")
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()

print(driver.title)
