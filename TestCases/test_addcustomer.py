import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.Logger import LoggenClass
from Utilities.readconfig import Readconfig
from pageObjects.AddCustPage import AddCustClass
from pageObjects.LoginPage import LoginClass


class Test_AddCust:
    Email=Readconfig.getemail()
    Pwd=Readconfig.getpwd()
    Log=LoggenClass.log_generator()

    @allure.story("Adding Customer")
    @allure.title("Add Customer Test Case")
    @allure.link("https://admin-demo.nopcommerce.com/")
    @allure.severity(allure.severity_level.NORMAL)

    @pytest.mark.nahid
    def test_add_customer(self,setup):
        self.Log.info("Test Case test_add_customer is started")
        self.driver = setup
        self.Log.info("Opening Browser & navigating to demo NOP_COMMERCE")
        self.lp = LoginClass(self.driver)
        self.Log.info("Entering email :" + self.Email)
        self.lp.Enter_email(self.Email)
        self.Log.info("Entering Password :" + self.Pwd)
        self.lp.Enter_pwd(self.Pwd)
        self.Log.info("Click on Loggin Button")
        self.lp.Clicklogin_btn()
        time.sleep(2)

        self.ac=AddCustClass(self.driver)
        self.Log.info("click on customer menu button")
        self.ac.Click_Customer_Menu_Button()
        time.sleep(2)
        self.Log.info("click on customer sub menu button")
        self.ac.Click_Customer_Sub_Menu_Button()
        self.Log.info("click on add customer button")
        self.ac.Click_Add_Customer_Button()
        email=Generate_Email()
        self.Log.info("Email :" + email)
        self.ac.Enter_Email(email)
        self.Log.info("Enter Password :" + self.Pwd)
        self.ac.Enter_PWD("Asdfgh@123")
        self.Log.info("Enter First Name")
        self.ac.Enter_Fname("test")
        self.Log.info("Enter Last Name")
        self.ac.Enter_Lname("demo")
        self.Log.info("Enter Gender")
        self.ac.Select_Gender("Male")
        self.Log.info("Enter DOB")
        self.ac.Enter_DOB("02/05/1996")
        self.Log.info("Enter Company Name")
        self.ac.Enter_Company_Name("xyz")
        self.Log.info("Click on is text exempt check box")
        self.ac.Check_Text()
        self.Log.info("Click on News Letter")
        self.ac.Click_News_Letter()
        self.Log.info("Click on News Letter List")
        self.ac.Click_News_Letter_List()
        # self.ac.Click_Customer_Roles()
        # self.ac.Click_Customer_Roles_List()
        self.Log.info("Select Value for Manager of Vendor")
        self.ac.Dropdown_Manager_of_vendor("Vendor 2")
        self.Log.info("Click on Active CheckBox ")
        self.ac.Check_Active()
        self.Log.info("Enter Comment")
        self.ac.Enter_Comment("All is Well!")
        self.Log.info("Click on Save Button ")
        self.ac.Click_Save_Button()
        time.sleep(2)

        if self.ac.Validate_Success_Msg()== "Pass":
            self.Log.info("Test Case test_add_customer is passed")
            self.driver.save_screenshot("..\\Screenshots\\test_add_customer_pass.png")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name='test_verify_url_pass',attachment_type=AttachmentType.PNG)
            self.Log.info("Taking Screenshot for allure")
            assert True
        else:
            self.Log.info("Test Case test_add_customer is failed")
            self.driver.save_screenshot("..\\Screenshots\\test_add_customer_fail.png")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name='test_verify_url_pass',attachment_type=AttachmentType.PNG)
            self.Log.info("Taking Screenshot for allure")
            assert False



def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=6))
    domain = random.choice(['gmail.com', 'outlook.com', 'ymail.com'])
    return  f"{username}@{domain}"

