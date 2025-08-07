from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import undetected_chromedriver as uc
from selenium_profiles.profiles import profiles
 

@pytest.fixture
def setup(browser):
    #driver = webdriver.Chrome()
    #serv_obj = Service(exceutable_path ="C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    
    if browser == "chrome":
        # profile = profiles.Windows()
        serv_obj = Service(exceutable_path ="C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        # driver = webdriver.Chrome(service =serv_obj, options=options,
        #         uc_driver=False, profile = profile
        #         )

        driver = webdriver.Chrome(service = serv_obj)

        #driver = uc.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Safari()
    return driver

def pytest_addoption(parser):  # this will get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request):# this will return browser value to setup method

    return request.config.getoption("--browser")

######Pytest HTML report
#It is a hook to add environment info in HTML report
def pytest_configure(config):
    config._metadata={"Project Name" : 'nop Commerce','Module Name' : 'Customers','Tester' :'Shinu'}

#It is a hook for delete/Modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None) # these details will be by default be displyed in report so we are removing that





