from selenium import webdriver
import time
import sys
sys.path.append('C:/Users/arspiedy/Desktop/selenium_tutorials/Project')

from autoscrapper.link_scrap  import scrap_link

(names,hrefs) = scrap_link("https://en.wikipedia.org/wiki/Walmart")
print("we are in testing function . ")
print(len(names))
for i in range(10):
	print(names[i],hrefs[i])