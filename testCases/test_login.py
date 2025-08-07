import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from testCases.conftest import setup
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUserName()
    Password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("**********Test_001_Login************")
        self.logger.info("**********Verify Homepage title************")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            self.logger.info("**********Verify Homepage title test is passed************")
            assert True
        else:
            self.driver.save_screenshot("C:/Users/shinu/SeleniumFramework/ScreenShots/test_homePageTitle.png")
            self.logger.error("**********Verify Homepage title test failed************")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********Verify login test started************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        time.sleep(10)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        self.driver.switch_to.frame(title="Widget containing a Cloudflare security challenge")
        self.driver.find_element(By.TAG_NAME,"input[@type = 'checkbox']").click()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**********Login Test is Passed************")
            assert True
        else:
            self.logger.error("**********Login Test is Failed************")
            self.driver.save_screenshot("C:/Users/shinu/SeleniumFramework/ScreenShots/test_login.png")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, setup):
        self.logger.info("**********Verify Logout Test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        self.driver.switch_to.frame(title="Widget containing a Cloudflare security challenge")
        self.driver.find_element(By.TAG_NAME,"input[@type = 'checkbox']").click()

        time.sleep(10)
        self.lp.clickLogout()

        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            self.logger.info("**********Verify Logout Test- Passed************")
            self.driver.close()
            assert True
        else:
            self.logger.error("**********Verify Logout Test -Failed ************")
            self.driver.save_screenshot("C:/Users/shinu/SeleniumFramework/ScreenShots/test_logout.png")
            self.driver.close()
            assert False


#pytest -v -s test_login.py
#pytest -v -s test_login.py --browser chrome
#pytest -v -s -n=3 test_login.py --browser chrome
#pytest -v -s -n=3 --html=Reports/report.html test_login.py --browser chrome


#to run the tests using markers
#pytest -s -v -m "sanity and regression" --html=Reports/report.html test_login.py --browser chrome
#pytest -s -v -m "sanity or regression" --html=Reports/report.html test_login.py --browser chrome
#pytest -s -v -m "sanity" --html=Reports/report.html test_login.py --browser chrome
        

