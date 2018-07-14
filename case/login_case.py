# coding: utf-8
import unittest

from selenium import webdriver
from pages.login_page import LoginPage
from public.screenshot import insert_img


class LoginCase(unittest.TestCase):
    def setUp(self):  # 每个用例执行之前执行
        # print('before test')
        self.dr = webdriver.Firefox()
        self.dr.get('http://localhost:9090/m4m')
        self.dr.maximize_window()
        self.dr.implicitly_wait(20)

    def tearDown(self):
        self.dr.quit()

    # dr = None
    #
    # @classmethod
    # def setUpClass(cls):  # 每个用例执行之前执行
    #     print('before test')
    #     cls.dr = webdriver.Firefox()
    #     cls.dr.maximize_window()
    #     cls.dr.implicitly_wait(10)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.dr.quit()

    def test_login_success(self):
        username = 'admin'
        password = 'Admin123'

        login_page = LoginPage(self.dr)
        login_page.url = 'http://localhost:9090/m4m/admin/index.jsp'
        login_page.navigate()
        dashboard_page = login_page.login(username, password)

        self.assertEqual('退出', dashboard_page.welcome_msg)
        insert_img(self.dr, "登录成功.jpg")

    def test_login_fail(self):
        """用户名或者密码错误"""
        username = 'admin2'
        password = 'Admin123'

        login_page = LoginPage(self.dr)
        login_page.url = 'http://localhost:9090/m4m/admin/index.jsp'
        login_page.navigate()
        login_page.login(username, password)
        self.assertEqual('账号或密码错误', login_page.error_msg)
        insert_img(self.dr, "账号或密码错误.jpg")


if __name__ == '__main__':
    unittest.main()
