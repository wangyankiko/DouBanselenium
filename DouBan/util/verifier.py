#! /usr/bin/env python
# -*- coding:utf-8 -*-
# created by wangyan on 2017/9/6

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def element_should_exist(driver=None, by ="xpath", value=None, wait_time = 15):
    try:
        if by =="xpath":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, value))
            )

        if by == "class":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, value))
            )

        if by == "name":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, value))
            )

        if by == "id":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.ID, value))
            )

    except NoSuchElementException:
        assert False

    assert True
