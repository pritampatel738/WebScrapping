from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:/Drivers/chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Walmart")

paragraphs = driver.find_elements_by_tag_name("p")
print(len(paragraphs))
texts = [i.text for i in paragraphs]
#print(texts)