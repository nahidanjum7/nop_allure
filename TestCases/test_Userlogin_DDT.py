import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities import ExcelMethods
from Utilities.Logger import LoggenClass
from Utilities.readconfig import Readconfig
from pageObjects.LoginPage import LoginClass


class Test_login_DDT:
    Log=LoggenClass.log_generator()
    Excel_File_Path="E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\TestData\\Test_Data.xlsx"

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.nahid
    def test_user_login_DDT(self,setup):
        self.Log.info("Test Case test_user_login_DDT is started")
        self.driver=setup
        self.Log.info("Opening Browser & navigating to demo NOP_COMMERCE")
        self.lp=LoginClass(self.driver)

        self.rows=ExcelMethods.numRows(self.Excel_File_Path,'LoginData')
        print("no of rows in Excel sheet : " + str(self.rows))
        Test_Case_Status_List = []
        for r in range(2,self.rows+1):  #iteration r=2
            self.Username = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 2)
            self.Password = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 3)
            self.Expected_Result = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 4)
            # self.Expected_Result = ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5,"This is my actual Result")
            # print("username : " + self.Username)
            # print("password : " + self.Password)
            # print("expected result : " + self.Expected_Result)

            self.Log.info("Entering Email" + self.Username)
            self.lp.Enter_email(self.Username)
            self.Log.info("Entering Password" + self.Password)
            self.lp.Enter_pwd(self.Password)
            self.Log.info("click on login button")
            self.lp.Clicklogin_btn()
            time.sleep(5)

            if self.lp.Verify_Login_Status() == "Login Pass":  # actual result #login hua h
                self.Log.info("Test Case test_Login is passed")
                ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")

                if self.Expected_Result == "Pass":  # expected result #pass:credentials right
                    self.Log.info("Expected result is passed")
                    Test_Case_Status_List.append("Pass")  # udating the status list by pass
                    self.driver.save_screenshot(
                        "E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_DDT_pass.png")
                    self.Log.info("Taking Screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_DDT_pass',
                                  attachment_type=AttachmentType.PNG)
                    self.Log.info("Taking Screenshot for allure")
                    self.lp.Clicklogout_btn()

                elif self.Expected_Result == "Fail":  # expected result #fail:credentials
                    self.Log.info("Expected result is failed")
                    Test_Case_Status_List.append("Fail")  # udating the status list by fail
                    ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")

                    self.driver.save_screenshot(
                        "E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_DDT_pass.png")
                    self.Log.info("Taking Screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_DDT_pass',
                                  attachment_type=AttachmentType.PNG)
                    self.Log.info("Taking Screenshot for allure")
                    self.lp.Clicklogout_btn()

            elif self.lp.Verify_Login_Status() == "Login Fail":  # actual result #login ni hua h
                self.Log.info("Test Case test_Login is failed")
                ExcelMethods.writeData(self.Excel_File_Path,'LoginData',r,5,"Fail")

                if self.Expected_Result == "Fail":  # expected result:credentials wrong
                    self.Log.info("Expected result is fail")
                    Test_Case_Status_List.append("Pass")  # udating the status list by pass
                    self.driver.save_screenshot(
                        "E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_DDT_fail.png")
                    self.Log.info("Taking Screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_DDT_fail',
                                  attachment_type=AttachmentType.PNG)
                    self.Log.info("Taking Screenshot for allure")
                    self.lp.Clicklogout_btn()

                elif self.Expected_Result == "Pass":  # expected result:credentials wrong pr b pass bol ra h
                    self.Log.info("Expected result is pass")
                    Test_Case_Status_List.append("Fail")  ##udating the status list by fail
                    ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Fail")

                    self.driver.save_screenshot(
                        "E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Screenshots\\test_user_login_DDT_fail.png")
                    self.Log.info("Taking Screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_DDT_fail',
                                  attachment_type=AttachmentType.PNG)
                    self.Log.info("Taking Screenshot for allure")
        print(Test_Case_Status_List)

        if "Fail" in Test_Case_Status_List:
            self.Log.info("Test Case test_user_login_DDT_fail is Failed")
            assert False

        else:
            self.Log.info("Test Case test_user_login_DDT_fail is Passed")
            assert True

        self.Log.info("Test Case test_user_login_DDT_fail is Completed")



















