# coding: utf-8
import unittest
import time
from pages.send_notice_page import NoticePage
from public.screenshot import insert_img
from case.base_case import BaseCase


class SendNoticeCase(BaseCase):

    # @unittest.skip
    def test_send_notice_success(self):
        """发送公告成功"""

        message = time.strftime("%Y_%m_%d_%H_%M_%S")
        notice_page = NoticePage(self.dr)
        notice_page.select_management_send_notice(message)
        self.assertIn('公告已下发', notice_page.send_notice_success_msg)
        # print(notice_page.send_notice_success_msg)
        insert_img(self.dr, "发送公告成功.jpg")

    def test_send_long_notice(self):
        """发送公告内容过长"""

        message = '很长很长的文字很长很长的文字很长很长的文字很长很长的文字' \
                  '很长很长的文字很长很长的文字很长很长的文字很长很长的文字很长很' \
                  '长的文字很长很长的文字很长很长的文字很长很长的文字很长很长的文字' \
                  '很长很长的文字很长很长的文字很长很长的文字很长很长的文字很长很长的文字' \
                  '很长很长的文字很长很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字' \
                  '很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字' \
                  '很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字很长的文字 '
        notice_page = NoticePage(self.dr)
        notice_page.select_management_send_notice(message)
        self.assertEqual('消息内容最多200个字！', notice_page.notice_long_msg)
        # print(notice_page.send_notice_success_msg)
        insert_img(self.dr, "公告过长.jpg")

    def test_send_null_notice(self):
        """发送公告为空"""

        message = ''
        notice_page = NoticePage(self.dr)
        notice_page.select_management_send_notice(message)
        self.assertIn('消息内容不能为空！', notice_page.address_null_msg)
        # print(notice_page.send_notice_success_msg)
        insert_img(self.dr, "公告内容为空.jpg")

    def test_send_null_address(self):
        """收件人为空"""

        message = time.strftime("%Y_%m_%d_%H_%M_%S")
        notice_page = NoticePage(self.dr)
        notice_page.null_management_send_notice(message)
        self.assertEqual('收件人不能为空！', notice_page.address_null_msg)
        # print(notice_page.send_notice_success_msg)
        insert_img(self.dr, "收件人为空.jpg")


if __name__ == '__main__':
    unittest.main()
    # # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(SendNoticeCase("test_send_null_notice"))
    # # suite.addTest(AddRoleCase("test_add_role_long"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
