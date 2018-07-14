import unittest
from selenium import webdriver
from pages.login_page import LoginPage


class BaseCase(unittest.TestCase):
    dr = None

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def setUp(self):  # 每个用例执行之前执行
        # print('before test')
        self.dr.get('http://localhost:9090/m4m')
        self.dr.maximize_window()
        self.dr.implicitly_wait(20)
        po = LoginPage(self.dr)
        po.login_success()

    def tearDown(self):
        self.dr.delete_all_cookies()
