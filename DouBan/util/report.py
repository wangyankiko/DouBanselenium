#!/usr/bin/env python
# -*- coding:utf-8 -*-

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
import time
import unittest
from DouBan.data import email_data
from DouBan.util import logger

# ************** send mail ****************

def sendReport(file_new):

     with open(file_new, 'rb') as f:
         mail_body = f.read()
         f.close()
         msg = MIMEText(mail_body, 'html', 'utf-8')
         # msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z", time.localtime(time.time()))
         msg['Subject'] = Header('The Report of DouBan', 'utf-8')
         msg['From'] = email_data.send_email
         msg['To'] = email_data.rec_email

         smtp = smtplib.SMTP('smtp.163.com')
         smtp.set_debuglevel(1)
         smtp.login(email_data.send_email, email_data.send_email_password)
         smtp.sendmail(msg['From'], msg['To'], msg.as_string())

         smtp.quit()
         logger.Log().info('test report has send out!')

def newReport(testReport):

    lists = os.listdir(testReport)
    print(lists)
    lists2 = sorted(lists)
    print(lists2)
    file_new = os.path.join(testReport, lists2[-1])


    return file_new

if __name__ == "__main__":
    base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    test_dir = base_path + '\cases'
    test_report_dir = base_path + '\\reports'

    os.path.exists(test_report_dir) or os.mkdir(test_report_dir)
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='execCase.py')
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    filename = test_report_dir + '\\' + now + 'Result.html'

    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream = fp, title = 'the report of DouBan ', description= 'the description:')
        runner.run(discover)
        fp.close()

        new_report = newReport(test_report_dir)
        sendReport(new_report)

