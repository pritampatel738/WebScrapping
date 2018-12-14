from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")


count_que = 10 # this is a parameter that controls the number of times we need to scrap.

def tag_find(site):
	"""
		Argument:
			This function accepts a site as an argument .
		Output:
			It returns 3 things .....
				(a)- The total number of tags
				(b)- The number of answers given
				(c)- The name of the link
				(d)- The total number of answers 
	"""
	print(site)
	driver.get(site)
	tag_array = [] # it contains the tags of a particular questions ....
	answer_arr = [] # it contains the answers of a particular question ....

	# finding the names of the tag .....
	val = driver.find_elements_by_css_selector("span[class='TopicName TopicNameSpan']")
	val1 = driver.find_elements_by_css_selector("span[class='TopicNameSpan TopicName']")
	#time.sleep(3)
	#print(type(val))
	#print(val)
	print("The tag_names are : ")
	if len(val) > 0:

		for i in range(len(val)):
			tag_array.append(val[i].text)

	if len(val1) > 0:

		for i in range(len(val1)):
			tag_array.append(val1[i].text)

	#for i in tag_array:
		#print(i)

	# start finding answer count ......
	try :

		answer_count = driver.find_element_by_css_selector("div[class='answer_count']")
	except:
		return (tag_array,0,"",answer_arr)

	
	# start finding the answer count ......
	string = answer_count.text
	ans_cnt = int(string[0])
	print("The total number of answers are : ",ans_cnt)

	# start finding the question_names ......
	que_name = driver.find_element_by_css_selector("span[class='rendered_qtext']").text


	# start finding the answers of each questions .....
	if ans_cnt >= 4:
		ans = driver.find_elements_by_css_selector("p[class='ui_qtext_para']")
		for i in range(len(ans)):
			answer_arr.append(ans[i].text)
			print(ans[i].text)

	return (tag_array,ans_cnt,que_name,answer_arr)
	

	


def refining_links(links):
	"""
		Argument:
			It takes an array as an argument.
		Output:
			It removes the duplicate from any array or list.
	"""
	refined_links = []
	refining_dict = {}
	for i in range(len(links)):
		if links[i] not in refining_dict.keys():
			refined_links.append(links[i])
		refining_dict[links[i]] = 1
	return refined_links


def rescrap(l,total_questions_count):
	"""Argument:
			This function accepts a site as an argument in "l" and total_questions_count .
		Output:
			It scraps that site and returns total number of questions that has been scraped till now.
	"""
	#names_array = []
	links_array = []
	driver.get(l)
	links = driver.find_elements_by_partial_link_text("GRE")
	#print(type(links))
	#print(len(links))
	string = "quora.com"
	for i in range(len(links)):
		temp_string = links[i].get_attribute('href') # store the link in temporary string.....
		if string in temp_string:
			links_array.append(temp_string)
			#names_array.append(links[i].text) # appending only those names that are quora sites ....
			print(temp_string)

	#refined_name = refining_links(names_array) # this is used to remover duplicate .....
	refined_link_array = refining_links(links_array)
	#print("The length of refined names are :",len(refined_name))
	print("The length of refined link array is : ",len(refined_link_array))

	#for i in refined_name:
		#total_unique_names.append(i) # appending total unique names to unique names array ........

	for i in refined_link_array:
		total_unique_links.append(i) # appending total unique links to unique links array .........

	
	total_questions_count += len(refined_link_array)
	print("The total_questions_count is : ",total_questions_count)
	return total_questions_count


def main(org_link,total_questions_count,total_unique_links):
	"""
		This is our main function.
		Argument:
			It takes an initial link to invoke the web browser.
		Output:
			It uses the function rescrap() to scrap the site till we get required number of questions.
	"""
	#names_array = []
	links_array = []
	driver.get(org_link)
	parent = driver.window_handles[0]
	# element = driver.find_element_by_id('id_of_the_link')
	# element.get_attribute('href')
	links = driver.find_elements_by_partial_link_text("GRE")
	print(type(links))
	print(len(links))
	string = "quora.com"
	for i in range(len(links)):
		if string in links[i].get_attribute('href'):

			links_array.append(links[i].get_attribute('href'))
			#names_array.append(links[i].text) # appending only those names that are quora sites ....

			print(links[i].get_attribute('href'))
	#refined_name = refining_links(names_array) # this is used to remover duplicate .....
	refined_link_array = refining_links(links_array)
	#print("The length of refined names are :",len(refined_name))
	print("The length of refined link array is : ",len(refined_link_array))

	#for i in refined_name:
		#total_unique_names.append(i) # appending total unique names to unique names array ........

	for i in refined_link_array:
		total_unique_links.append(i) # appending total unique links to unique links array .........

	
	total_questions_count += len(refined_link_array)
	print("The total_questions_count is : ",total_questions_count)

	while total_questions_count <= count_que:
		if total_questions_count >= count_que:
			#print("The length of unique names are : ",len(total_unique_names))
			print("The length of unique links are : ",len(total_unique_links))
			driver.switch_to_window(parent)
			#driver.quit()
			break
		for i in refined_link_array:
			if total_questions_count >= count_que:
				continue
			total_questions_count = rescrap(i,total_questions_count)

	#total_unique_names = refining_links(total_unique_names)
	total_unique_links = refining_links(total_unique_links)

	print("The total unique links are : ",len(total_unique_links))
	#print("The total unique names are : ",len(total_unique_names))
	for i in range(5):
		print(total_unique_links[i])

	return total_unique_links


def print_values(names,links,tag_dict,answer_dict):

	for i in range(5):
		print("The name of the site is : ",names[i])
		print("The actual link of the site is : ",links[i])
		print("The tags are : ")
		tag_arr = tag_dict[links[i]]
		for k in range(len(tag_arr)):
			print(tag_arr[k])

		answer_arr = answer_dict[links[i]]
		print("The answers are : ")
		for j in range(len(answer_arr)):
			print(answer_arr[j])


if __name__ == "__main__":

	total_questions_count = 0  # it counts how many question we've scrapped .....
	total_unique_links = [] # it contains the original unique links .......
	#total_unique_names = [] # it contains the total unique names ......
	total_unique_links = main("https://www.quora.com/What-is-GRE-How-can-I-prepare-for-it",total_questions_count,total_unique_links)
	#for i in range(len(total_unique_names)):
	print("Inside main function")
	print(len(total_unique_links))
	for i in total_unique_links:
		print(i)

	final_names_array = [] # it contains the names of the links that has 4 or more answers ....
	final_links_array = [] # it contains the original links .....
	tag_dict = {} # this dictionary maps the original link with it's corresponding tag names .....
	answer_dict = {} # this is a dictionary that stores the answers for each question ......

	for i in total_unique_links:
		(temp_tag,que_count,name,temp_answers) = tag_find(i) # tag_find returns the tag_name array,the number of answers and name of the link ...
		if que_count >= 4:
			final_names_array.append(name)
			final_links_array.append(i)
			tag_dict[i] = temp_tag
			answer_dict[i] = temp_answers

	print("The length of final_names_array is : ",len(final_names_array)) # printing the length of the names_array ...
	print("The length of final_links_array is : ",len(final_links_array)) # printing the length of the links array ...
	print("The length of tag_dict keys is : ",len(tag_dict.keys())) # printing the size of the tag_dict ...
	print("The length of answer_dict is : ",len(answer_dict)) # printing the size of the answer_dict .....

	print_values(final_names_array,final_links_array,tag_dict,answer_dict)
	driver.quit()