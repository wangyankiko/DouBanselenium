#! /usr/bin/env python
# -*- coding:utf-8 -*-
#created by wangyan on 2017/9/6

from DouBan.cases.BaseCase import BaseCase
from DouBan.util import logger
from DouBan.data import login_page
from DouBan.elements import element
from DouBan.bussiness import Action
from DouBan.util import verifier
from DouBan.data import login_page

class loginCase(BaseCase):

    # test case of login
    def test_email_login(self):
        self.get_url(self.webbroswer.driver, login_page.page_url)
        self.webbroswer.driver.get_screenshot_as_file('C:\Program Files (x86)\\1.png')
        self.email_login(self.webbroswer.driver)


    #define get_url
    def get_url(self, driver, page_url):
        Action.get_url(driver, page_url)
        verifier.element_should_exist(driver, by="id", value=login_page.email_loc)

    def email_login(self, driver):
        Action.email_login(driver)