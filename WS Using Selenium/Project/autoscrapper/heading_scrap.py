from selenium import webdriver
import time
import pandas as pd

def scrap_headings(site,number=100):

	driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
	driver.get(site)

	headings1 = driver.find_elements_by_tag_name("h1")
	headings2 = driver.find_elements_by_tag_name("h2")
	headings3 = driver.find_elements_by_tag_name("h3")
	headings4 = driver.find_elements_by_tag_name("h4")
	headings5 = driver.find_elements_by_tag_name("h5")
	headings6 = driver.find_elements_by_tag_name("h6")

	heading_names = [] # used to store the link names ......
	#print("The length of headings are :",len(headings))

	for i in range(len(headings1)): 
		#print(i)
		heading_names.append(headings1[i].text) # append the name of the link .....

	for i in range(len(headings2)): 
		#print(i)
		heading_names.append(headings2[i].text) # append the name of the link .....

	for i in range(len(headings3)): 
		#print(i)
		heading_names.append(headings3[i].text) # append the name of the link .....

	for i in range(len(headings4)): 
		#print(i)
		heading_names.append(headings4[i].text) # append the name of the link .....

	for i in range(len(headings5)): 
		#print(i)
		heading_names.append(headings5[i].text) # append the name of the link .....

	for i in range(len(headings6)): 
		#print(i)
		heading_names.append(headings6[i].text) # append the name of the link .....
		
	#print("outside link loop")
	if(len(heading_names) > number): # to make the number of links requested ......
		heading_names = heading_names[:number] 
		

	return heading_names
	