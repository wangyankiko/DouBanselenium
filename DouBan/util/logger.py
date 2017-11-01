#! /usr/bin/env python
# -*-coding:utf-8 -*-
#created by wangyan on 2017/9/6

import logging
import os
import time

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# print(base_path)
log_path = base_path+"\log"
# print(log_path)

#create a handler for writing log
class Log:
    def __init__(self):
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        self.filename = log_path + '\\' + now +'log.txt'
    def __printconsole(self, level, message):

        #create a logger 记录器
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        #create a handler for writing log
        fh = logging.FileHandler(self.filename)
        fh.setLevel(logging.DEBUG)

        # create another handler for console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #define formatter

        formatter = logging.Formatter('%(asctime)s [%(levelname)s]:%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #add handler to logger

        logger.addHandler(fh)
        logger.addHandler(ch)

        #follow a log

        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == "error":
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning',message)

    def error(self, message):
        self.__printconsole('error', message)

