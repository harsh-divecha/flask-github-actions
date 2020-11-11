
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

class Test(unittest.TestCase):
	def testName(self):
		driver = webdriver.Chrome(ChromeDriverManager().install())
		#driver.implicitly_wait(10)
		driver.get("https://tranquil-crag-81243.herokuapp.com/")
		driver.maximize_window()
		msg=driver.find_element(By.TAG_NAME , "body")
		try:
			pass
			#WebDriverWait(driver, timeout=3).until(EC.title_contains('SeleniumHQ Browser Automation'))
			#WebDriverWait(driver, timeout=3).until(EC.)
		except Exception as e: 
			print (e)
		# print(f"---{driver.title}---")
		# titleOfWebPage=driver.title
		print(msg.text)
		#breakpoint()
		self.assertEqual("Hello, Vaibhav!", msg.text, "webpage title is not matching")
		driver.quit()
if __name__ == "__main__":
	print('inside Main')
	unittest.main()
	#driver.quit()