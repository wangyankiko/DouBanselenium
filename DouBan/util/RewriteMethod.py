#!/usr/bin/env python
# -*- coding:utf-8 -*-

#created by wangyan on 2017/9/9

def max_window(driver):
    '''
    set broswer window maxinized.
    Usage:
    driver.max_window()
    :return:
    '''
    driver.maximize_window()


def set_window_size(driver, wide, high):
    '''
    set broswer window wide and high
    Usage:
    driver.set_window_size(wide,high)
    :param driver:
    :param wide:
    :param high:
    :return:
    '''
    driver.set_window_size(wide, high)

