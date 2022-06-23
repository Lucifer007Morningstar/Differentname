from selenium.webdriver.common.by import By


class SearchCustomer:
    link_customersmenu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    text_email_id="SearchEmail"
    text_fname_id="SearchFirstName"
    text_lname_id="SearchLastName"

    button_search_id="search-customers"
    table_xpath="//div[@id='customers-grid_wrapper']"
    tableRows_xpath="//div[@id='customers-grid_wrapper']//tbody//tr"
    tableColumns_xpath="//div[@id='customers-grid_wrapper']//tbody//tr//td"
    link_search_xpath="//div[@class='search-text']"
    def __init__(self,driver):
        self.driver = driver

    def searchButton(self):
        self.driver.find_element(By.XPATH,self.link_search_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.text_email_id).clear()
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.text_fname_id).clear()
        self.driver.find_element(By.ID, self.text_fname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID, self.text_lname_id).clear()
        self.driver.find_element(By.ID, self.text_lname_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//div[@id='customers-grid_wrapper']//tbody//tr["+str(r)+"]//td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//div[@id='customers-grid_wrapper']//tbody//tr["+str(r)+"]//td[3]").text
            if name==Name:
                flag=True
                break
        return flag



