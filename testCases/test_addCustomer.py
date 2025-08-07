import string
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
import random


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUserName()
    Password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def tes_addCustomer(self, setup):
        self.driver = setup




    def random_generator(size=8, chars=string.ascii_lowercase +string.digits):
        return ''.join(random.choice(chars) for x in range(size))
        