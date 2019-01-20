from selenium import webdriver
import time
import sys
sys.path.append('C:/Users/arspiedy/Desktop/selenium_tutorials/Project')

from autoscrapper.heading_scrap  import scrap_headings

headings = scrap_headings("https://en.wikipedia.org/wiki/Walmart")
print("we are in testing function . ")
print(len(headings))
for i in range(10):
	print(headings[i])