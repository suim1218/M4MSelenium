# coding: utf-8
import unittest
from time import sleep
import time
from case.base_case import BaseCase
from public.screenshot import insert_img
from pages.internet_control_page import BlackPage


class AddBlacklistCase(BaseCase):

    # @unittest.skip
    def test_add_blacklist_success(self):
        """添加黑名单成功"""

        black_list_name = black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        self.assertEqual('添加成功', black_page.add_black_list_success_msg)
        # print(black_page.first_row.text)
        # print(black_list_name)
        insert_img(self.dr, "添加黑名单成功.jpg")

    def test_add_another_blacklist_success(self):
        """继续添加黑名单成功"""

        black_list_name = black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        sleep(2)
        black_page.continue_add_black_list(black_list_name, black_list_url)
        self.assertEqual('添加成功', black_page.add_black_list_success_msg)
        insert_img(self.dr, "继续添加黑名单成功.jpg")

    # @unittest.skip
    def test_blacklist_name_null(self):
        """黑名单名称为空"""

        black_list_name = ''
        black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        self.assertEqual('名称不能为空', black_page.black_name_null_msg)
        insert_img(self.dr, "黑名单名称为空.jpg")

    # @unittest.skip
    def test_blacklist_url_null(self):
        """黑名单网址为空"""

        black_list_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_list_url = ''
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        self.assertEqual('网址不能为空', black_page.blacklist_url_null_msg)
        insert_img(self.dr, "黑名单网址为空.jpg")

    # @unittest.skip
    def test_blacklist_name_and_url_null(self):
        """黑名单名称和网址都为空"""

        black_list_name = ''
        black_list_url = ''
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        self.assertEqual('名称不能为空', black_page.black_name_null_msg)
        self.assertEqual('网址不能为空', black_page.blacklist_url_null_msg)
        insert_img(self.dr, "黑名单名称和网址都为空.jpg")

    def test_blacklist_longname(self):
        """黑名单名称过长"""

        black_list_name = '超过20位超过20位超过20位超过20位超过20位超过20位超过20位'
        black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        self.assertEqual('长度不超过 20 位', black_page.blacklist_longname_msg)
        insert_img(self.dr, "黑名单名称过长.jpg")

    def test_blacklist_long_url(self):
        """黑名单网址过长"""

        black_list_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_list_url = '超过50位超过50位超过50位超过50位超过50位超过50位超过50位超过50位超过50位超过50位超过50位超过50位超过50' \
                         '超过50位超过50位超过50位超过50位位超过50位'
        black_page = BlackPage(self.dr)
        black_page.add_black_list(black_list_name, black_list_url)
        self.assertEqual('长度不超过 50 位', black_page.blacklist_long_url_msg)
        insert_img(self.dr, "黑名单网址过长.jpg")

    def test_developing_strategy(self):
        """下发策略成功"""

        black_page = BlackPage(self.dr)
        black_page.develop_black_list()
        # print(black_page.develop_success_msg)
        self.assertEqual('操作成功', black_page.develop_success_msg)
        insert_img(self.dr, "下发黑名单策略成功.jpg")

    def test_import_blacklist(self):
        """导入黑名单成功"""

        black_page = BlackPage(self.dr)
        black_page.import_black_list('F:\\M4MUI\\web_control.xlsx')
        # print(black_page.upload_files_success_msg)
        # self.assertEqual('操作成功', black_page.upload_files_success_msg)
        self.assertEqual('操作成功', black_page.upload_files_success_msg)
        insert_img(self.dr, "导入黑名单成功.jpg")

    def test_import_blacklist_null(self):
        """导入黑名单名称为空"""

        black_page = BlackPage(self.dr)
        black_page.import_black_list('F:\\M4MUI\\web_control2.xlsx')
        # print(black_page.upload_files_success_msg)
        # self.assertEqual('操作成功', black_page.upload_files_success_msg)
        self.assertIn('名称不能为空', black_page.upload_files_success_msg)
        insert_img(self.dr, "导入黑名单名称为空.jpg")

    '''
    def test_delete_first_blacklist(self):
        """删除第一行黑名单"""
        po = LoginPage(self.dr)
        po.login_success()
        black_page = BlackPage(self.dr)
        black_list_name = black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_page.add_black_list(black_list_name, black_list_url)
        black_page.return_btn.click()
        sleep(1.5)
        black_page.delete_first_row_black_list()
        # print(black_page.blacklist_null_msg)
        self.assertEqual('没有找到匹配的记录', black_page.blacklist_null_msg)

        insert_img(self.dr, "删除第一行黑名单.jpg")
    '''

    def test_delete_first_page_blacklist(self):
        """删除第一页黑名单"""

        black_page = BlackPage(self.dr)
        black_list_name = black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        black_page.add_black_list(black_list_name, black_list_url)
        black_page.return_btn.click()
        sleep(1)
        black_page.delete_first_page_black_list()
        sleep(1.5)
        self.assertEqual('没有找到匹配的记录', black_page.blacklist_null_msg)
        insert_img(self.dr, "删除第一页黑名单.jpg")

    '''
    def test_edit_first_page_blacklist(self):
        """编辑第一行黑名单"""
        po = LoginPage(self.dr)
        po.login_success()
        black_page = BlackPage(self.dr)
        black_page.blacklist_page()
        black_page.delete_first_page_black_list()

        # black_list_name = black_list_url = time.strftime("%Y_%m_%d_%H_%M_%S")
        # black_page.add_black_list(black_list_name, black_list_url)
        # black_page.select_first_blacklist.click()
        # black_page.return_btn.click()
        #
        # sleep(1)
        # sleep(1.5)
        # # self.assertEqual('没有找到匹配的记录', black_page.blacklist_null_msg)
        # # insert_img(self.dr, "删除第一页黑名单.jpg")
        #
    '''


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # # suite.addTest(AddBlacklistCase("test_delete_first_blacklist"))
    # suite.addTest(AddBlacklistCase("test_add_another_blacklist_success"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
