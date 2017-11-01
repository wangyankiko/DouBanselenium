#! /usr/bin/env python
# -*- coding：utf-8 -*-
#created by wangyan on 2017/9/6

import unittest
from DouBan.cases.loginCase import loginCase


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(loginCase("test_email_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()