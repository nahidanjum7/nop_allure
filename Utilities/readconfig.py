import configparser

config=configparser.RawConfigParser()
config.read("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getemail():
        Email=config.get('login data','email')
        return Email
    @staticmethod
    def getpwd():
        Pwd=config.get('login data','pwd')
        return Pwd


