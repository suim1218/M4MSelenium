# coding: utf-8
import unittest
import time
from pages.send_wensi_page import WensiPage
from public.screenshot import insert_img
from case.base_case import BaseCase


class SendWensiCase(BaseCase):

    # @unittest.skip
    def test_send_wensi_success(self):
        """发送闻思成功"""

        title = content = time.strftime("%Y_%m_%d_%H_%M_%S")
        wensi_page = WensiPage(self.dr)
        wensi_page.send_wensi(title, content)
        self.assertEqual(title, wensi_page.return_describe)
        self.assertIn('发布', wensi_page.return_result)
        # print(wensi_page.return_result)
        insert_img(self.dr, "发送闻思成功.jpg")

    def test_wensi_title_null(self):
        """闻思标题为空"""

        title = ''
        content = time.strftime("%Y_%m_%d_%H_%M_%S")
        wensi_page = WensiPage(self.dr)
        wensi_page.save_wensi(title, content)
        self.assertEqual('闻思标题不能为空', wensi_page.wensi_title_or_content_null_msg)
        # print(wensi_page.wensi_title_or_content_null_msg)
        insert_img(self.dr, "闻思标题为空.jpg")

    def test_wensi_title_long(self):
        """闻思标题过长"""

        title = '很长很长的闻思标题很长很长的闻思标题很长很长的闻思标题很长很长的' \
                '闻思标题很长很长的闻思标题很长很长的闻思标题很长很长的闻思标题很长很长的闻思标题很长很长的闻思标题很长很长的闻思标题'
        content = time.strftime("%Y_%m_%d_%H_%M_%S")
        wensi_page = WensiPage(self.dr)
        wensi_page.save_wensi(title, content)
        self.assertEqual('闻思标题不超过64位', wensi_page.wensi_title_long_msg)
        # print(wensi_page.wensi_title_long_msg)
        insert_img(self.dr, "闻思标题过长.jpg")

    def test_wensi_content_null(self):
        """闻思内容为空"""

        title = time.strftime("%Y_%m_%d_%H_%M_%S")
        content = ''
        wensi_page = WensiPage(self.dr)
        wensi_page.save_wensi(title, content)
        self.assertEqual('闻思内容不能为空', wensi_page.wensi_title_long_msg)
        # print(wensi_page.wensi_title_long_msg)
        insert_img(self.dr, "闻思内容为空.jpg")

    def test_save_wensi(self):
        """保存闻思不发布"""

        title = content = time.strftime("%Y_%m_%d_%H_%M_%S")
        wensi_page = WensiPage(self.dr)
        wensi_page.save_wensi_and_return(title, content)
        self.assertEqual(title, wensi_page.return_describe)
        self.assertIn('未发布', wensi_page.return_result)
        # print(wensi_page.return_result)
        # print(wensi_page.return_describe)
        insert_img(self.dr, "保存闻思不发布.jpg")

    def test_edit_wensi(self):
        """编辑闻思"""

        title = content = time.strftime("%Y_%m_%d_%H_%M_%S")
        new_title = new_content = '二次编辑'
        wensi_page = WensiPage(self.dr)
        wensi_page.edit_wensi(title, content, new_title, new_content)
        self.assertEqual(new_title, wensi_page.return_describe)
        self.assertIn('发布', wensi_page.return_result)
        # print(wensi_page.return_result)
        # print(wensi_page.return_describe)
        insert_img(self.dr, "二次编辑闻思.jpg")

    def test_delete_wensi(self):
        """删除闻思"""

        title = content = time.strftime("%Y_%m_%d_%H_%M_%S")
        wensi_page = WensiPage(self.dr)
        wensi_page.delete_wensi(title, content)
        self.assertEqual('操作成功', wensi_page.delete_success_msg)
        # print(wensi_page.delete_success_msg)
        insert_img(self.dr, "删除闻思.jpg")


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(SendWensiCase("test_delete_wensi"))
    # # suite.addTest(AddRoleCase("test_add_role_long"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
