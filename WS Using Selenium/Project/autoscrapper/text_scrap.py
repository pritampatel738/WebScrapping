from selenium import webdriver
import time
import pandas as pd
#site = input("Input the website : ")

def scrap_text(site,sent=100):
	driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
	driver.get(site)

	paragraphs= driver.find_elements_by_tag_name("p")
	time.sleep(4)
	sent_arr= []
	#print(paragraphs.text)
	#print(type(paragraphs))
	sent_count = 0 # used for counting the total number of sentences scrapped ....
	for i in range(len(paragraphs)):

		temp_string = paragraphs[i].text # get the text of that paragraph section ....
		temp_string1 = temp_string.split(".") # splitting the sentences on comma ....

		for j in temp_string1: # iterate in splitted text based on full stop ....
			sent_arr.append(j)
			sent_count = sent_count + 1

			if(sent_count >= sent):
				return sent_arr

		if sent_count >= sent:
			return sent_arr



	#time.sleep(10000)

def make_csv(sent):
	




