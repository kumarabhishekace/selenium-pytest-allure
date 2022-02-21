from lib2to3.pgen2 import driver
from selenium import webdriver

class webdriver_obj():
    def __init__(self):
        pass

    def driver_obj(self):
        self.driver = webdriver.Chrome('./chromedriver')
        return self.driver
