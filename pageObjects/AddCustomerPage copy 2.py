class AddCustomer:

    firstlines_xpath = "//i[@class='fa fa-bars']"
    selectcutsomers_xpath = "//body/div[@class='wrapper']/aside[@class='main-sidebar sidebar-dark-primary elevation-4']/div[@class='sidebar']/nav[@class='mt-2']/ul[@role='menu']/li[4]/a[1]"
    selectcustomers2_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    txtemail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtfirstname_xpath = "//input[@id='FirstName']"
    txtlastname_xpath = "//input[@id='LastName']"
    radiogender_male_xpath ="//input[@id='Gender_Male']"
    radiogender_female_xpath = "//input[@id='Gender_Female']"
    txtcompanyname_xpath = "//input[@id='Company']"
    checkboxistaxexempt_xpath = "//input[@id='Company']"
    dropdownnewsletter_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"



    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        
