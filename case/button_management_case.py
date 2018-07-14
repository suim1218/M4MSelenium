# coding: utf-8
# import unittest
import time
from public.screenshot import insert_img
from case.base_case import BaseCase
from pages.button_management_page import ButtonPage


class ButtonCase(BaseCase):

    # @unittest.skip
    def test_add_button_success(self):
        """添加按钮成功"""

        button_name = button_code = time.strftime("%Y_%m_%d_%H_%M_%S")
        button_page = ButtonPage(self.dr)
        button_page.add_button(button_name, button_code)
        self.assertIn('成功', button_page.add_button_success_msg)
        # print(button_page.add_button_success_msg)
        insert_img(self.dr, "添加按钮成功.jpg")

    def test_button_name_null(self):
        """按钮名称为空"""

        button_name = ''
        button_code = time.strftime("%Y_%m_%d_%H_%M_%S")
        button_page = ButtonPage(self.dr)
        button_page.add_button(button_name, button_code)
        self.assertIn('名称不能为空', button_page.button_name_null_msg)
        # print(button_page.button_name_null_msg)
        insert_img(self.dr, "按钮名称为空.jpg")

    def test_button_name_long(self):
        """按钮名称过长"""

        button_name = '很长很长的按钮名称很长很长的按钮名称很长很长的按钮名称很长很长的按钮名称'
        button_code = time.strftime("%Y_%m_%d_%H_%M_%S")
        button_page = ButtonPage(self.dr)
        button_page.add_button(button_name, button_code)
        self.assertIn('长度不超过30位', button_page.button_name_long_msg)
        # print(button_page.button_name_long_msg)
        insert_img(self.dr, "按钮名称过长.jpg")

    def test_button_code_null(self):
        """按钮编码为空"""

        button_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        button_code = ''
        button_page = ButtonPage(self.dr)
        button_page.add_button(button_name, button_code)
        self.assertIn('编号不能为空', button_page.button_code_null_msg)
        # print(button_page.button_code_null_msg)
        insert_img(self.dr, "按钮编码为空.jpg")

    def test_button_code_long(self):
        """按钮编码过长"""

        button_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        button_code = '很长很长的编码很长很长的编码很长很长的编码很长很长的编码很长很长的编码很长很长的编码'
        button_page = ButtonPage(self.dr)
        button_page.add_button(button_name, button_code)
        self.assertIn('长度不超过30位', button_page.button_code_long_msg)
        # print(button_page.button_code_long_msg)
        insert_img(self.dr, "按钮编码过长.jpg")

    def test_button_code_repeat(self):
        """按钮编码存在"""

        button_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        button_code = 'btn-add'
        button_page = ButtonPage(self.dr)
        button_page.add_button(button_name, button_code)
        self.assertEqual('编码已经存在', button_page.button_code_repeat_msg)
        # print(button_page.button_code_repeat_msg)
        insert_img(self.dr, "按钮编码重复.jpg")

    def test_query_button_name(self):
        """根据正确的按钮名称查询"""

        button_name = '注销'
        button_code = ''
        button_page = ButtonPage(self.dr)

        button_page.query_information(button_name, button_code)

        self.assertIn(button_name, button_page.return_result)
        insert_img(self.dr, "根据按钮名称查询.jpg")

    def test_query_button_error_name(self):
        """根据错误的按钮名称查询"""

        button_name = '注销33'
        button_code = ''
        button_page = ButtonPage(self.dr)
        button_page.query_information(button_name, button_code)
        # print(a)
        self.assertEqual('没有找到匹配的记录', button_page.null_msg)
        # print(button_page.null_msg)
        insert_img(self.dr, "根据错误的按钮名称查询.jpg")

    def test_query_button_code(self):
        """根据正确的按钮编码查询"""

        button_name = ''
        button_code = 'btn-zhuxiao'

        button_page = ButtonPage(self.dr)

        button_page.query_information(button_name, button_code)
        # print(a)
        self.assertIn(button_code, button_page.return_result)
        insert_img(self.dr, "根据按钮编码查询.jpg")

    def test_query_button_error_code(self):
        """根据错误的按钮编码查询"""

        button_name = ''
        button_code = '注销33'

        button_page = ButtonPage(self.dr)

        button_page.query_information(button_name, button_code)
        # print(a)
        self.assertEqual('没有找到匹配的记录', button_page.null_msg)
        # print(button_page.null_msg)
        insert_img(self.dr, "根据错误的按钮编码查询.jpg")

    def test_query_name_and_code_error(self):
        """根据错误的按钮名称和编码查询"""

        button_name = '123123'
        button_code = '注销33'

        button_page = ButtonPage(self.dr)

        button_page.query_information(button_name, button_code)
        # print(a)
        self.assertEqual('没有找到匹配的记录', button_page.null_msg)
        # print(button_page.null_msg)
        insert_img(self.dr, "根据错误的按钮名称和编码查询.jpg")


if __name__ == '__main__':
    unittest.main()
    # # 构造测试集
    # suite = unittest.TestSuite()
    # # suite.addTest(ButtonCase("test_button_code_null"))
    # suite.addTest(ButtonCase("test_query_button_error_code"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
