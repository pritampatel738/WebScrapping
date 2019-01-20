from selenium import webdriver
import time




def download_videos(arr):
	driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
	driver.maximize_window()
	driver.get("https://en.savefrom.net/")

	for i in arr:
		driver.find_element_by_xpath("//div[@class='tarea-wrap']/input").send_keys(i)
		time.sleep(5)
		driver.find_element_by_xpath("//div[@class='r-box']/button").click()
		time.sleep(10)
		driver.find_element_by_partial_link_text("Download").click()
		time.sleep(15)


	pass


def main():
	arr = ["https://www.youtube.com/watch?v=FVZkk4cF6fo&list=PLRAV69dS1uWQEbcHnKbLldvzrjdOcOIdY&index=2"]

	download_videos(arr)

	pass


if __name__ == "__main__":

	main()
	pass

