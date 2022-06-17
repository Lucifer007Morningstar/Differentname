from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    # baseURL="https://admin-demo.nopcommerce.com/login"
    # username="admin@yourstore.com"
    # password="admin"
    baseURL=ReadConfig.getApplicationURL()
    username =ReadConfig.getUserename()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        # self.driver=webdriver.Chrome(executable_path="C:\\browser\\chromedriver.exe")
        self.logger.info("**Test_001_Login**")
        self.logger.info("**Verifing home page title**")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        # self.driver.close()
        if act_title=='Your store. Login':
            assert True
            self.driver.save_screenshot(".\\Screenshots\\"+"passedcase.png")
            self.driver.close()
            self.logger.info("**Homepage title test is passsed**")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            self.logger.error("**Homepasge title test is failed**")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loign(self,setup):
        # self.driver=webdriver.Chrome(executable_path="C:\\browser\\chromedriver.exe")
        self.logger.info("**Verifing Login test**")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPasswordName(self.password)
        self.lp.ButtonLogin()
        title=self.driver.title
        # self.driver.close()
        if title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("sdf")
            self.driver.close()
            self.logger.info("**Login test is passed**")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("**Login test is failed**")
            assert False

