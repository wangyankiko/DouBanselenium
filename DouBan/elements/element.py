#!/usr/bin/env python
# - * - coding: utf-8 -*-
#created by wangyan on 2017/9/6

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Element:

    def __init__(self,driver = None,by = None, value = None):
        self.driver = driver
        self.by     = by
        self.value  = value

    def get_element(self, wait_time = 15):

        element = None
        if self.by == "xpath":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.value))
            )

        elif self.by == "class":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.value))
            )

        elif self.by == "css_selector":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.value))
            )

        elif self.by == "name":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, self.value))
            )
        elif self.by == "id":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, self.value))
            )

        return element

    def click(self):
        self.get_element().click()

    def input_value(self, value = None):
        self.get_element().send_keys(value)

    # def send_value(self, value = None):
    #     self.get_element().click().send_keys(value)