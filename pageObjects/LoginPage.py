import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginClass:
    Text_email_xpath="//input[@id='Email']"
    Text_pwd_xpath="//input[@id='Password']"
    Click_LoginButton_xpath="//button[@type='submit']"
    Click_LogoutButton_xpath="//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)



    def Enter_email(self,email):
        self.driver.find_element(By.XPATH, self.Text_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.Text_email_xpath).send_keys(email)

    def Enter_pwd(self,pwd):
        self.driver.find_element(By.XPATH, self.Text_pwd_xpath).clear()
        self.driver.find_element(By.XPATH,self.Text_pwd_xpath).send_keys(pwd)

    def Clicklogin_btn(self):
        self.driver.find_element(By.XPATH,self.Click_LoginButton_xpath).click()

    def Clicklogout_btn(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.Click_LogoutButton_xpath)))
            self.driver.find_element(By.XPATH, self.Click_LogoutButton_xpath).click()
        except:
            pass

    def Verify_Login_Status(self):
        try:
            self.driver.find_element(By.XPATH, self.Click_LogoutButton_xpath)
            return "Login Pass"
        except:
            return "Login Fail"


# pytest -v --html=Htmlreports/newhtmlreport.html --alluredir="E:\New Files\Framework\Framewok(Selenium)\nopcom_project\AllureReports" --browser chrome