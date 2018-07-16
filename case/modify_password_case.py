# coding: utf-8
import unittest
from pages.modify_password_page import ModifyPasswordPage
from case.base_case import BaseCase
from public.screenshot import insert_img


class ModifyPasswordCase(BaseCase):

    # @unittest.skip
    def test_old_password_null(self):
        """原密码为空"""

        old_password = ''
        new_password = again_password = 'admin123456'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码不能为空', modify_password_page.old_password_null_msg)
        # print(modify_password_page.old_password_null_msg)
        insert_img(self.dr, "修改密码原密码为空.jpg")

    def test_new_password_null(self):
        """新密码为空"""

        old_password = ''
        new_password = ''
        again_password = 'admin123456'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码不能为空', modify_password_page.new_password_null_msg)
        # print(modify_password_page.new_password_null_msg)
        insert_img(self.dr, "修改密码新密码为空.jpg")

    def test_again_password_null(self):
        """确认新密码输入框为空"""

        old_password = ''
        new_password = 'admin123456'
        again_password = ''
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码不能为空', modify_password_page.new_password_again_null_msg)
        # print(modify_password_page.new_password_null_msg)
        insert_img(self.dr, "修改密码确认新密码输入框为空.jpg")

    def test_different_password(self):
        """两次密码输入不一致"""

        old_password = ''
        new_password = 'admin123456'
        again_password = 'admin12345'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('两次密码不一致', modify_password_page.different_password_msg)
        # print(modify_password_page.different_password_msg)
        insert_img(self.dr, "修改密码两次密码输入不一致.jpg")

    def test_new_password_long(self):
        """新密码过长"""

        old_password = ''
        new_password = 'admin123456123456123456123456123456123456'
        again_password = 'admin123456123456123456123456123456123456'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码是6-30位', modify_password_page.new_password_long_msg)
        # print(modify_password_page.new_password_long_msg)
        insert_img(self.dr, "新密码过长.jpg")

    def test_new_password_short(self):
        """新密码过短"""

        old_password = ''
        new_password = ''
        again_password = 'admin'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码是6-30位', modify_password_page.new_password_short_msg)
        # print(modify_password_page.new_password_long_msg)
        insert_img(self.dr, "新密码过短.jpg")

    def test_new_password_number_type(self):
        """新密码只为数字类型"""

        old_password = ''
        new_password = '111111'
        again_password = '111111'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码至少包含数字、字母或符号中的两种', modify_password_page.new_password_one_type)
        # print(modify_password_page.new_password_one_type)
        insert_img(self.dr, "新密码为纯数字.jpg")

    def test_new_password_letter_type(self):
        """新密码只为字母类型"""

        old_password = ''
        new_password = 'aaaaaa'
        again_password = 'aaaaaa'
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertEqual('密码至少包含数字、字母或符号中的两种', modify_password_page.new_password_one_type)
        # print(modify_password_page.new_password_one_type)
        insert_img(self.dr, "新密码为纯字母.jpg")

    def test_new_password_success(self):
        """修改密码成功"""

        old_password = new_password = again_password = ''
        modify_password_page = ModifyPasswordPage(self.dr)
        modify_password_page.modify_password(old_password, new_password, again_password)
        self.assertIn('操作成功', modify_password_page.modify_password_success_msg)
        # print(modify_password_page.modify_password_success_msg)
        insert_img(self.dr, "修改密码成功.jpg")


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(ModifyPasswordCase("test_new_password_success"))
    # # suite.addTest(ModifyPasswordCase("test_new_password_letter_type"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
