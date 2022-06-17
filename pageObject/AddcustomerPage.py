import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    link_customers_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menu_item_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_addnew_xpath="//a[normalize-space()='Add new']"
    textfield_Email_id="Email"
    textfield_Password_id="Password"
    textfield_Firstname_id="FirstName"
    textfield_Lastname_id="LastName"
    radiobutton_Male_id="Gender_Male"
    radiobutton_Female_id="Gender_Female"
    textfield_DOB_xpath="//input[@id='DateOfBirth']"
    textfield_companyname_xpath="//input[@id='Company']"
    checkbox_intax_exempt_xpath = "//input[@id='IsTaxExempt']"
    lsTitle_storename_xpath="//li[normalize-space()='Your store name']"
    lsTitle_teststore_xpath="//li[normalize-space()='Test store 2']"
    checkbox_active_xpath="//input[@id='Active']"
    textfield_Admin_comment_xpath="//textarea[@id='AdminComment']"
    txtcustomerRole_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath="//li[normalize-space()='Administrators']"
    lstitemForum_Moderators_xpath="//li[normalize-space()='Forum Moderators']"
    lstitemGuests_xpath="//li[normalize-space()='Guests']"
    lstitemRegistered_xpath="//li[normalize-space()='Registered']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    dropdown_manager_of_vendor_xpath="//select[@id='VendorId']"
    button_save_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomesMenu(self):
        self.driver.find_element(By.XPATH,self.link_customers_xpath).click()
        time.sleep(3)

    def clickOnCustomesMenuItem(self):
        self.driver.find_element(By.XPATH,self.link_customer_menu_item_xpath).click()
        time.sleep(2)
    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.link_addnew_xpath).click()
        time.sleep(2)
    def setEmail(self,email):
        self.driver.find_element(By.ID, self.textfield_Email_id).send_keys(email)

    def setPassword(self,Passward):
        self.driver.find_element(By.ID,self.textfield_Password_id).send_keys(Passward)

    def setCustomerRoles(self,text):
        self.driver.find_element(By.XPATH,"//select[@id='SelectedCustomerRoleIds']").click()

        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.txtcustomerRole_xpath).clear()
        if text=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif text=='Administrator':
            self.listitem=self.driver.find_element(By.XPATH, "//option[normalize-space()='Administrators']")
        elif text == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//li[2]//span[2]").click()
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif text == "Registered":
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif text=="Vendors":
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerofVendor(self,value):
        drop=Select(self.driver.find_element(By.XPATH,self.dropdown_manager_of_vendor_xpath))
        drop.select_by_visible_text(value)

    def setGender(self,name):
        if name=="Male":
            self.driver.find_element(By.XPATH,self.radiobutton_Male_id).click()
        elif name=="Female":
            self.driver.find_element(By.XPATH, self.radiobutton_Female_id).click()
        else:
            self.driver.find_element(By.XPATH, self.radiobutton_Male_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.textfield_Firstname_id).send_keys(fname)

    def setLAstName(self,lname):
        self.driver.find_element(By.ID,self.textfield_Lastname_id).send_keys(lname)

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.textfield_DOB_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH, self.textfield_companyname_xpath).send_keys(companyname)

    def setAdmininContent(self,content):
        self.driver.find_element(By.XPATH,self.textfield_Admin_comment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()













