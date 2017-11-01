#! /usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from DouBan.data import email_data
import unittest
import time, os

def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    smtpserver = "smtp.163.com"
    msg = MIMEMultipart()
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('the test report of douban', 'utf-8')
    msg.attach(text)

    #send attach

    msg['Subject'] = Header('the test of douban', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file['Content-Disposition'] = 'attachment; filename="testReport.html" '
    msg.attach(msg_file)
    msg['from'] =email_data.send_email
    msg['To'] = email_data.rec_email
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(email_data.send_email, email_data.send_email_password)
    smtp.sendmail(msg['from'], msg['To'], msg.as_string())
    smtp.quit()

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
        runner = HTMLTestRunner(stream = fp, title = 'the report of PGC ', description= 'the description:')
        runner.run(discover)
        fp.close()

        new_report = newReport(test_report_dir)
        send_mail(new_report)
