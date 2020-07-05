from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class loginPage:
    #Login and logout Locators

    username="LoginUser_UserName"
    password="LoginUser_Password"
    loginxp="//input[@class='btn btn-block btn-lg amulet']"
    event="/html/body/div[1]/div[2]/div[1]/div/div[4]/div/div/div[2]/div[1]/div[4]/img[2]"
    evsum="//img[@class='info_event']"
    evdetails="html/body/div[6]/div/div[2]/ul/li[2]/img"
    eventdesc="//img[@class='description']"
    cloudy="//label[contains(text(),'Cloudy')]"
    desc="//textarea[@name='description']"
    testdata="Hello Test Data"
    Okbtn="//*[@id='ui-id-7']/table/tbody/tr[2]/td/div/form/div[3]/div/div/input[1]"
    logoutmark="//*[@title='Operator']"
    logoutbt="//a[contains(text(),'Log Out')]"
    yes="//button[@id='bot2-Msg1']"

#Dead Code
    # filter="//*[@id='Page']/div/div[1]/div/div[1]/button[1]"
    # unplanned="//div[contains(text(),'Unplanned Events')]"
    #userbtn = "/html/body/div[2]/div/div[1]/div/md-toolbar[3]/div/div[6]/span/button/img"
    #logout = "//a[contains(text(),'Logout')]"


    def __init__(self,driver):
        self.driver=driver

    def setuserID(self,username):
        self.driver.find_element_by_id(self.username).send_keys(username)

    def setpwd(self,password):
        self.driver.find_element_by_id(self.password).send_keys(password)

    def login(self):
        try:
            self.driver.find_element_by_xpath(self.loginxp).click()
        except:
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/button[1]").click()
            print("An Error Occurred")

    def clickevent(self):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.event)))
            element.click()
        except Exception as err:
            print(err,"No element found")

    def clickevensum(self):
        self.driver.find_element_by_xpath(self.evsum).click()
        self.driver.save_screenshot("C:\\Users\LENOVO\\Desktop\\Varun Personal\\ITMS_app\Screenshots\\Event_Summary.png")

    def clickevendetails(self):
        try:
            self.driver.find_element_by_xpath(self.evdetails).click()
        except Exception as err:
            self.driver.save_screenshot("C:\\Users\LENOVO\\Desktop\\Varun Personal\\ITMS_app\Screenshots\\Event_Details.png")
            return err

    def clickeventdesc(self):
        try:
            self.driver.find_element_by_xpath(self.eventdesc).click()
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.eventdesc)))
            element.click()
            self.driver.find_element_by_xpath(self.cloudy).click()
            self.driver.find_element_by_xpath(self.desc).send_keys(self.testdata)
            self.driver.find_element_by_xpath(self.Okbtn).click()
            self.driver.save_screenshot("C:\\Users\LENOVO\\Desktop\\Varun Personal\\ITMS_app\Screenshots\\Event_Description.png")
        except Exception as err:
            print(err, "Element is not found")

    def logout(self):
        self.driver.find_element_by_xpath(self.logoutmark).click()
        self.driver.find_element_by_xpath(self.logoutbt).click()
        #self.driver.switch_to.alert.accept()
        self.driver.find_element_by_xpath(self.yes).click()
