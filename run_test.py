import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from public.new_report import file
import yagmail


def send_mail(file):
    yag = yagmail.SMTP(user="18662764778@163.com", password="sui1218", host='smtp.163.com')
    # 邮箱正文
    title = "M4M后台管理测试报告"
    contents = ["M4M后台管理测试报告,请注意查收，详情请看附件"]
    yag.send('18662764778@163.com', title, contents, [file])


if __name__ == '__main__':
    testreport = "./report/"  # 测试报告目录
    suit = unittest.defaultTestLoader.discover("./case", "*_case.py")

    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(testreport + now_time + "_report.html", "wb")

    runner = HTMLTestRunner(stream=fp, title="M4M后台管理测试报告", description="window7,firefox")
    runner.run(suit)
    fp.close()  # 关闭报告文件
    send_mail(file)

