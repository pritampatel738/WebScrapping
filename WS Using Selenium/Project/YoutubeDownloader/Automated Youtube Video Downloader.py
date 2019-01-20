from selenium import webdriver
import time


class Downloader:

	def __init__(self,arr):
		self.arr = arr



	def download_videos(self):

		self.driver = webdriver.Chrome("D:/Drivers/chromedriver.exe")
		self.driver.maximize_window()
		self.driver.get("https://en.savefrom.net/")

		for i in self.arr:
			self.driver.find_element_by_xpath("//div[@class='tarea-wrap']/input").clear()
			self.driver.find_element_by_xpath("//div[@class='tarea-wrap']/input").send_keys(i)
			time.sleep(5)
			self.driver.find_element_by_xpath("//div[@class='r-box']/button").click()
			time.sleep(10)
			self.driver.find_element_by_partial_link_text("Download").click()
			#self.driver.back()
			time.sleep(15)

		self.driver.sleep(1000000000)

def main():
	

	# create an array of links (this is the manual part only) ......
	arr = ["https://www.youtube.com/watch?v=FVZkk4cF6fo&list=PLRAV69dS1uWQEbcHnKbLldvzrjdOcOIdY&index=2","https://www.youtube.com/watch?v=8mm3hAbsusQ"]

	# make an instance of downloader class ........
	download = Downloader(arr)
	download.download_videos()


if __name__ == "__main__":
	main()
