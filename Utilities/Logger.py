import inspect
import logging
import inspect

class LoggenClass:
    @staticmethod
    def log_generator():
        log_name=inspect.stack()[1][3] #getting file name -class-method
        logger=logging.getLogger(log_name) #generating logs
        logfile=logging.FileHandler("E:\\New Files\\Framework\\Framewok(Selenium)\\nopcom_project\\Logs\\nop_com_logs.log") #log file
        log_format=logging.Formatter("%(asctime)s : %(levelname)s:	%(name)s :%(funcName)s: %(lineno)d: %(message)s") #log format
        logfile.setFormatter(log_format) #setting format to logs
        logger.addHandler(logfile) #adding log everytime on same file
        logger.setLevel(logging.INFO) #setting log level
        return logger


