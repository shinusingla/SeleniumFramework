import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage

from selenium.webdriver.common.by import By


import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData.xlsx"
    Username = ReadConfig.getUserName()
    Password = ReadConfig.getPassword()
    logger = LogGen.loggen()



    
    def test_login_ddt(self, setup):
        self.logger.info("**********class Test_002_Login_DDT:************")
        self.logger.info("**********Verify login test started************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows =XLUtils.getRowCount(self.path,"Sheet1")
        self.columns =XLUtils.getColumnCount(self.path,"Sheet1")
        lst_status =[]
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.driver.find_element(By.TAG_NAME,"input[@type = 'checkbox']").click()
            time.sleep(5)
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp =="Pass":
                    self.logger.info("**********Login Test is Passed************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp =="Fail":
                    self.logger.info("**********Login Test is Failed************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            else:
                if self.exp =="Pass":
                    self.logger.info("**********Login Test is Failed************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp =="Fail":
                    self.logger.info("**********Login Test is Passed************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("**********Login Data Test is Passed************")
                assert True
            else:
                self.logger.info("**********Login DATA Test is Failed************")
                assert False

        self.driver.close()
        self.logger.info("**********END of Login DATA Test************")
       


   

#pytest -v -s test_login.py
#pytest -v -s test_login.py --browser chrome
#pytest -v -s -n=3 test_login.py --browser chrome
#pytest -v -s -n=3 --html=Reports/report.html test_login.py --browser chrome

        

