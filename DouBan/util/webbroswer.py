#!/usr/bin/env python
# -*- coding:utf-8 -*-
#created by wangyan

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities

class webutils():

    def __init__(self, browser='firfox'):
        '''

        :param browser: browser pattern
        '''
        if browser == "firefox":
            driver = webdriver.Firefox()

        elif browser == "chrome":
            driver = webdriver.Chrome()

        elif browser == "ie":
            DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
            driver = webdriver.Ie()

        try:
            self.driver = driver
        except Exception:
            raise NameError("not found this browser,you can enter 'firfox,'chrome','ie'")



    # def quit(self):
    #      self.driver.quit()
    #
    # def get(self, url):
    #     self.driver.get(url)
    #
    # def find_element(self, *by):
    #     self.driver.find_element(*by)