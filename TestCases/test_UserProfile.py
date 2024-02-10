import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.Logger import LoggenClass
from Utilities.readconfig import Readconfig
from pageObjects.LoginPage import LoginClass

@allure.feature('Page_Title')
@allure.story('Verifying the Page Title')
@allure.issue('xyz-456')
@allure.link('https://admin-demo.nopcommerce.com/',name='nopCommerce Website')
@allure.title('nop Com-Test Page Title')
@allure.description('My test Description')
@allure.severity(allure.severity_level.CRITICAL)
class Test_Userprofile:
    Email=Readconfig.getemail()
    Pwd=Readconfig.getpwd()
    Log=LoggenClass.log_generator()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.nahid
    def test_verify_url(self,setup):
        self.Log.info("Test Case test_verify_url is started")
        self.driver=setup
        self.Log.info("Opening Browser & navigating to demo NOP_COMMERCE")
        Page_Title=self.driver.title
        self.Log.info("Page Title is: " + self.driver.title)

        # print(Page_Title)

        if Page_Title == "Your store. Login":
            self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_verify_url_pass.png")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name='test_verify_url_pass',attachment_type=AttachmentType.PNG)
            self.Log.info("Taking Screenshot for allure")
            assert True
        else:
            self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_verify_url_fail.png")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name='test_verify_url_fail',attachment_type=AttachmentType.PNG)
            self.Log.info("Taking Screenshot for allure")
            assert False
        self.Log.info("Test Case test_verify_url is Completed")

    @pytest.mark.nahid
    def test_Login(self,setup):
        self.Log.info("Test Case test_Login is started")
        self.driver=setup
        self.Log.info("Opening Browser & navigating to demo NOP_COMMERCE")
        self.lp=LoginClass(self.driver)
        self.Log.info("Entering email :" + self.Email)
        self.lp.Enter_email(self.Email)
        self.Log.info("Entering Password :" + self.Pwd)
        self.lp.Enter_pwd(self.Pwd)
        self.Log.info("Click on Loggin Button")
        self.lp.Clicklogin_btn()
        if self.lp.Verify_Login_Status()=="Login Pass":
            self.Log.info("Test Case test_Login is passed")
            self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_Login_pass.png")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name='test_Login_pass',attachment_type=AttachmentType.PNG)
            self.Log.info("Taking Screenshot for allure")
            self.lp.Clicklogout_btn()
            assert True
        else:
            self.Log.info("Test Case test_Login is passed")
            self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_Login_fail.png")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name='test_Login_fail',attachment_type=AttachmentType.PNG)
            self.Log.info("Taking Screenshot for allure")
            assert False
        self.Log.info("Test Case test_Login is Completed")











