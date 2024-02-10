
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class AddCustClass:
        Click_Customer_Menu_XPATH="//a[@href='#']//p[contains(text(),'Customers')]"
        Click_Customer_Sub_Menu_XPATH="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
        Click_Add_Customer_XPATH="//a[normalize-space()='Add new']"
        Text_Email_XPATH="//input[@id='Email']"
        Text_Password_XPATH="//input[@id='Password']"
        Text_Fname_XPATH = "//input[@id='FirstName']"
        Text_Lname_XPATH = "//input[@id='LastName']"
        Radio_Male_XPATH = "//input[@id='Gender_Male']"
        Radio_Female_XPATH = "//input[@id='Gender_Female']"
        Calender_XPATH="//input[@id='DateOfBirth']"
        Text_Company_Name_XPATH="//input[@id='Company']"
        CheckBox_Text_XPATH="//input[@id='IsTaxExempt']"
        Click_News_Letter_XPATH="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
        Click_News_Letter_List_XPATH="//li[normalize-space()='Test store 2']"
        # Click_Customer_Roles_XPATH="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
        # Click_Customer_Roles_List_Xpath="// li[contains(text(), 'Vendors')]"
        Dropdown_Manager_of_Vendor_XPATH="//select[@id='VendorId']"
        CheckBox_Active_XPATH="//input[@id='Active']"
        Text_Comment_XPATH="//textarea[@id='AdminComment']"
        Click_Save_Button_Xpath="//button[@name='save']"
        Text_Success_Msg_XPATH=" / html / body / div[3] / div[1] / div[1]"




        def __init__(self,driver):
            self.driver=driver


        def Click_Customer_Menu_Button(self):
            self.driver.find_element(By.XPATH,self.Click_Customer_Menu_XPATH).click()

        def Click_Customer_Sub_Menu_Button(self):
            self.driver.find_element(By.XPATH,self.Click_Customer_Sub_Menu_XPATH).click()

        def Click_Add_Customer_Button(self):
            self.driver.find_element(By.XPATH,self.Click_Add_Customer_XPATH).click()

        def Enter_Email(self,email):
            self.driver.find_element(By.XPATH,self.Text_Email_XPATH).send_keys(email)

        def Enter_PWD(self,pwd):
            self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(pwd)

        def Enter_Fname(self,fname):
            self.driver.find_element(By.XPATH, self.Text_Fname_XPATH).send_keys(fname)

        def Enter_Lname(self,lname):
            self.driver.find_element(By.XPATH, self.Text_Lname_XPATH).send_keys(lname)

        def Select_Gender(self,gender):
            if gender =="Male":
                self.driver.find_element(By.XPATH,self.Radio_Male_XPATH).click()
            else:
                self.driver.find_element(By.XPATH,self.Radio_Female_XPATH).click()

        def Enter_DOB(self,date):
            self.driver.find_element(By.XPATH, self.Calender_XPATH).send_keys(date)

        def Enter_Company_Name(self,cname):
            self.driver.find_element(By.XPATH, self.Text_Company_Name_XPATH).send_keys(cname)

        def Check_Text(self):
            self.driver.find_element(By.XPATH, self.CheckBox_Text_XPATH).click()

        def Click_News_Letter(self):
            self.driver.find_element(By.XPATH, self.Click_News_Letter_XPATH).click()

        def Click_News_Letter_List(self):
            self.driver.find_element(By.XPATH, self.Click_News_Letter_List_XPATH).click()

        # def Click_Customer_Roles(self):
        #     self.driver.find_element(By.XPATH, self.Click_Customer_Roles_XPATH).click()
        #
        # def Click_Customer_Roles_List(self):
        #     self.driver.find_element(By.XPATH, self.Click_Customer_Roles_List_Xpath).click()

        def Dropdown_Manager_of_vendor(self,value):
            Select(self.driver.find_element(By.XPATH, self.Dropdown_Manager_of_Vendor_XPATH)).select_by_visible_text(value)

        def Check_Active(self):
            self.driver.find_element(By.XPATH, self.CheckBox_Active_XPATH).click()

        def Enter_Comment(self,comment):
            self.driver.find_element(By.XPATH, self.Text_Comment_XPATH).send_keys(comment)

        def Click_Save_Button(self):
            self.driver.find_element(By.XPATH, self.Click_Save_Button_Xpath).click()

        def Validate_Success_Msg(self):
            try:
                self.driver.find_element(By.XPATH, self.Text_Success_Msg_XPATH)
                print("test case Passed")
                return "Pass"
            except:
                print("test case Failed")
                return "Fail"









