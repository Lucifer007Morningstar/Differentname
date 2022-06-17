from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_loign_ddt(self,setup):
        self.logger.info("***TEst 0002 login data**")
        self.logger.info("**Verifing Login test**")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)


        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Numbers of rows in an Excel: ",self.rows)
        lst_status=[]#Empty List

        for r in range(2,self.rows+1):
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.SetUserName(self.username)
            self.lp.SetPasswordName(self.password)
            self.lp.ButtonLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("**PAssed**")
                    self.lp.ButtonLogout();
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("**Test case Failed**")
                    self.lp.ButtonLogout();
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("**Failed**")
                    lst_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("**PAssed**")
                    lst_status.append("pass")

        if "fail" not in lst_status:
                self.logger.info("Login ddt tst is failed")
                self.driver.close()
                assert True
        else:
                self.logger.info("Login ddt test failed")
                self.driver.close()
                assert False


        self.logger.info("end of login DDT Test")
        self.logger.info("Copmleted TC_Login DDTT_002")





















        #