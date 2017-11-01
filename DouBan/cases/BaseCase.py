# /usr/bin/env python
# -*-coding:utf-8 -*-
#created by wangyan 2017.09.06

import unittest
from selenium import webdriver
from DouBan.data import webdriver_url
from DouBan.data import login_page
from DouBan.util.webbroswer import webutils

class BaseCase(unittest.TestCase):
    def setUp(self):
        #to do
        self.webbroswer = webutils('chrome')
        # self.driver.get(login_page.page_url)
        # print(self.driver.title)

    def tearDown(self):
        #to do
        self.webbroswer.driver.quit()


