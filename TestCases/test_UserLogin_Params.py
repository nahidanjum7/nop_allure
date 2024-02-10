import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.Logger import LoggenClass
from Utilities.readconfig import Readconfig
from pageObjects.LoginPage import LoginClass


class Test_login_Params:
    Log=LoggenClass.log_generator()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.nahid
    def test_user_login_params(self,setup,DataForLogin):
        self.Log.info("Test Case test_user_login_params is started")
        self.driver=setup
        self.Log.info("Opening Browser & navigating to demo NOP_COMMERCE")
        self.lp=LoginClass(self.driver)
        self.Log.info("Entering email :" + DataForLogin[0])
        self.lp.Enter_email(DataForLogin[0])
        self.Log.info("Entering Password :" +DataForLogin[1])
        self.lp.Enter_pwd(DataForLogin[1])
        self.Log.info("Click on Login Button")
        self.lp.Clicklogin_btn()

        Test_Case_Status_List = []

        if self.lp.Verify_Login_Status()=="Login Pass": #actual result #login hua h
            self.Log.info("Test Case test_Login is passed")

            if DataForLogin[2]=="Pass": #expected result #pass:credentials right
                self.Log.info("Expected result is passed")
                Test_Case_Status_List.append("Pass") #udating the status list by pass
                self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_params_pass.png")
                self.Log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(),name='test_user_login_params_pass',attachment_type=AttachmentType.PNG)
                self.Log.info("Taking Screenshot for allure")
                self.lp.Clicklogout_btn()

            elif DataForLogin[2]=="Fail": #expected result #fail:credentials
                self.Log.info("Expected result is failed")
                Test_Case_Status_List.append("Fail") #udating the status list by fail
                self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_params_pass.png")
                self.Log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_params_pass',attachment_type=AttachmentType.PNG)
                self.Log.info("Taking Screenshot for allure")
                self.lp.Clicklogout_btn()

        elif self.lp.Verify_Login_Status()=="Login Fail": #actual result #login ni hua h
            self.Log.info("Test Case test_Login is failed")

            if DataForLogin[2]=="Fail": #expected result:credentials wrong
                self.Log.info("Expected result is fail")
                Test_Case_Status_List.append("Pass") #udating the status list by pass
                self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_params_fail.png")
                self.Log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_params_fail',attachment_type=AttachmentType.PNG)
                self.Log.info("Taking Screenshot for allure")
                self.lp.Clicklogout_btn()

            elif DataForLogin[2]=="Pass": #expected result:credentials wrong pr b pass bol ra h
                self.Log.info("Expected result is pass")
                Test_Case_Status_List.append("Fail") ##udating the status list by fail
                self.driver.save_screenshot("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_params_fail.png")
                self.Log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_params_fail',attachment_type=AttachmentType.PNG)
                self.Log.info("Taking Screenshot for allure")

        print(Test_Case_Status_List)

        if "Pass" in Test_Case_Status_List:
            self.Log.info("Test Case test_user_login_params is Passed")
            assert True
        else:
            self.Log.info("Test Case test_user_login_params is Failed")
            assert False

        self.Log.info("Test Case test_user_login_params is Completed")














