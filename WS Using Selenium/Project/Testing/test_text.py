from selenium import webdriver
import time
import sys
sys.path.append('C:/Users/arspiedy/Desktop/selenium_tutorials/Project')

from autoscrapper.text_scrap  import scrap_text

sent = scrap_text("https://en.wikipedia.org/wiki/Walmart")
print("we are in testing function . ")
print(len(sent))
for i in range(10):
	print(sent[i])