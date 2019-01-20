from selenium import webdriver
import time
import sys
sys.path.append('C:/Users/arspiedy/Desktop/selenium_tutorials/Project')

from autoscrapper.image_scrap  import scrap_image

headings = scrap_image("https://en.wikipedia.org/wiki/Walmart")
