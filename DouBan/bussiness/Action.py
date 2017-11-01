#! /usr/bin/env python
# -*-coding:utf-8 -*-
#created by wangyan on 2017/9/6

from DouBan.elements.element import Element
from DouBan.data import login_page
from DouBan.data import email_data

#获取页面地址
def get_url(driver,page_url):
    driver.get(page_url)


def email_login(driver):
    Element(driver, by="id", value=login_page.email_loc).input_value(email_data.email_num)
    Element(driver, by="id", value=login_page.password_loc).input_value(email_data.password)
    Element(driver, by="class", value=login_page.login_loc).click()

