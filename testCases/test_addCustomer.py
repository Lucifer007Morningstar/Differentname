import pytest

from pageObject.AddcustomerPage import AddCustomer
from pageObject.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random




class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserename()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("**Test_003_Add_customer**")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPasswordName(self.password)
        self.lp.ButtonLogin()
        self.logger.info("**Login Succesfull**")
        self.logger.info("**Starting Add Customer test**")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomesMenu()
        self.addcust.clickOnCustomesMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("**Provide customer details**")

        self.email=random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)

        self.addcust.setPassword("test1234")
        # self.addcust.setCustomerRoles("Administrator")
        # self.addcust.setManagerofVendor("Vendor2")
        # self.addcust.setGender("Male")
        self.addcust.setFirstName("Lucifer")
        self.addcust.setLAstName("Morningstar")
        self.addcust.setDOB("12/18/1990")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdmininContent("This is testing for....")
        self.addcust.clickOnSave()

        self.logger.info("**Save the info**")

        self.logger.info("**add customer validation started**")
        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has been added successfully.'in self.msg:
            assert  True==True
            self.logger.info("**Add customer test passed**")
        else:
            self.driver.save_screenshot(".\\Screensots\\"+"test_addCustomer_scr.png")
            self.logger.info("**Add customer test failed**")
            assert True==False
        self.driver.close()
        self.logger.info("**Ending home page title test**")


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

