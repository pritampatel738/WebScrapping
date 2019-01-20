from selenium import webdriver
import time
import pandas as pd

def scrap_link(site,number=100):

	driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
	driver.get(site)

	links = driver.find_elements_by_tag_name("a")
	#print(type(links))
	link_href = [] # used to store the actual links ......
	link_names = [] # used to store the link names ......

	for i in range(len(links)): # it takes a little while ......
		print(i)
		link_href.append(links[i].get_attribute("href")) # append actual links ...
		link_names.append(links[i].text) # append the name of the link .....
		
	print("outside link loop")
	if(len(link_names) > number): # to make the number of links requested ......
		link_names = link_names[:number] 
		link_href = link_href[:number]

	return (link_names,link_href)
	