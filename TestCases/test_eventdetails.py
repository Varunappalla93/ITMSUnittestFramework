import unittest
from selenium import webdriver
import sys
import time
from selenium.webdriver import ActionChains
from PageObjects.PageObjects import loginPage

sys.path.append("C:/Users/LENOVO/Desktop/Varun Personal/ITMS_app")

class Eventdettest(unittest.TestCase):
    url="https://hyd-itms.ibigroup.in/login"
    username="operator"
    password="123"
    driver=webdriver.Chrome("C:/Users/LENOVO/Desktop/Varun Personal/ITMS_app/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_eventdet(self):
        lp = loginPage(self.driver)
        lp.setuserID(self.username)
        lp.setpwd(self.password)
        lp.login()
        time.sleep(20)
        lp.clickevendetails()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()


