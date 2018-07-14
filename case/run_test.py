# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
import time, os

if __name__ == '__main__':
    testreport = "../report/"  # 测试报告目录
    suit = unittest.defaultTestLoader.discover("./", "*_case.py")

    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(testreport + now_time + "_report.html", "wb")

    runner = HTMLTestRunner(stream=fp, title="M4M后台管理测试报告", description="window7,firefox")
    runner.run(suit)
    fp.close()  # 关闭报告文件
    # report = new_file(testreport)  # 找到最新的测试报告
    # send_mail(report)    # 发送测试报告到指定邮箱
