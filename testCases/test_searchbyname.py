from pageObject.AddcustomerPage import AddCustomer
from pageObject.LoginPage import LoginPage
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time


class search_By_name_Test_OO5:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserename()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def searchbyname(self,setup):
        self.logger.info("**Search Customer by Email_005**")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPasswordName(self.password)
        self.lp.ButtonLogin()

        self.logger.info("**Login Succesfull**")
        self.logger.info("**Starting search Customer test**")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomesMenu()
        self.addcust.clickOnCustomesMenuItem()
        time.sleep(3)
        self.logger.info("**Starting search Customer test by name**")
        searchcust = SearchCustomer(self.driver)
        # searchcust.searchButton()
        # time.sleep(2)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.ClickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("**TC is passed**")
        self.driver.close()

