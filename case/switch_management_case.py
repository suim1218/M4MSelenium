# coding: utf-8
import unittest
import time
from pages.switch_management_page import SwitchPage
from public.screenshot import insert_img
from case.base_case import BaseCase


class SwitchCase(BaseCase):

    # @unittest.skip
    def test_add_switch_success(self):
        """添加设备开关成功"""

        switch_name = switch_key = switch_code = '1'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertIn('操作成功', switch_page.add_switch_success_msg)
        # print(switch_page.add_switch_success_msg)
        insert_img(self.dr, "添加设备开关成功.jpg")

    def test_switch_name_null(self):
        """开关名称为空"""

        switch_name = ''
        switch_key = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_code = '代号1'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('请填写必填项目', switch_page.switch_name_null_msg)
        # print(switch_page.add_switch_success_msg)
        insert_img(self.dr, "开关名称为空.jpg")

    def test_switch_long_name(self):
        """开关名称过长"""

        switch_name = '很长很长的开关名称很长很长的开关名称很长很长的开关名称很长很长的开关名称'
        switch_key = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_code = '代号1'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('长度不超过 20 位', switch_page.switch_name_long_msg)
        # print(switch_page.add_switch_success_msg)
        insert_img(self.dr, "开关名称过长.jpg")

    def test_switch_key_null(self):
        """开关编码为空"""

        switch_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_key = ''
        switch_code = '代号1'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('编码不能为空', switch_page.switch_key_null_msg)
        # print(switch_page.add_switch_success_msg)
        insert_img(self.dr, "开关编码为空.jpg")

    def test_switch_long_key(self):
        """开关编码过长"""

        switch_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_key = '很长很长的开关编码很长很长的开关编码很长很长的开关编码' \
                     '很长很长的开关编码很长很长的开关编码很长很长的开关编码' \
                     '很长很长的开关编码很长很长的开关编码很长很长的开关编码很长很长的开关编码'
        switch_code = '代号1'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('长度不超过 50 位', switch_page.switch_key_long_msg)
        # print(switch_page.switch_key_long_msg)
        insert_img(self.dr, "开关编码过长.jpg")

    def test_switch_repeat_key(self):
        """开关编码重复"""

        switch_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_key = 'luyin'
        switch_code = '代号1'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('编码不能重复', switch_page.switch_key_repeat_msg)
        # print(switch_page.switch_key_long_msg)
        insert_img(self.dr, "开关编码重复.jpg")

    def test_switch_code_null(self):
        """开关代号为空"""

        switch_name = switch_key = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_code = ''

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('开关代号不能为空', switch_page.switch_code_null_msg)
        # print(switch_page.add_switch_success_msg)
        insert_img(self.dr, "开关代号为空.jpg")

    def test_switch_long_code(self):
        """开关代号过长"""

        switch_name = switch_key = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_code = '很长很长的代号很长很'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('长度不超过 8 位', switch_page.switch_code_long_msg)
        # print(switch_page.switch_code_long_msg)
        insert_img(self.dr, "开关代号过长.jpg")

    def test_switch_repeat_code(self):
        """开关代号重复"""

        switch_name = switch_key = time.strftime("%Y_%m_%d_%H_%M_%S")
        switch_code = '10080000'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        self.assertEqual('开关代号不能重复', switch_page.switch_code_repeat_msg)
        # print(switch_page.switch_code_long_msg)
        insert_img(self.dr, "开关代号重复.jpg")

    def test_delete_switch(self):
        """新增一个开关后删除"""

        switch_name = switch_key = switch_code = '100861'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)
        switch_page.delete_switch()
        self.assertEqual('操作成功', switch_page.delete_msg)
        # print(switch_page.delete_msg)
        insert_img(self.dr, "删除开关.jpg")

    def test_aedit_switch(self):
        """新增一个开关后编辑"""

        switch_name = switch_key = switch_code = '100862'

        switch_page = SwitchPage(self.dr)
        switch_page.add_switch(switch_name, switch_key, switch_code)

        new_switch_name = new_switch_key = new_switch_code = '100863'

        switch_page.edit_switch(new_switch_name, new_switch_key, new_switch_code)
        self.assertIn('操作成功', switch_page.add_switch_success_msg)
        # print(switch_page.delete_msg)
        insert_img(self.dr, "编辑开关.jpg")

    def test_select_switch_type(self):
        """添加管控开关"""

        switch_name = switch_key = switch_code = '1111'
        switch_page = SwitchPage(self.dr)
        switch_page.select_switch_type(switch_name, switch_key, switch_code)
        self.assertIn('操作成功', switch_page.add_switch_success_msg)
        insert_img(self.dr, "添加管控开关.jpg")

    def test_query_switch_name(self):
        """根据正确的开关名称查询"""

        switch_name = '录音'
        switch_code = ''
        switch_page = SwitchPage(self.dr)

        switch_page.query_information(switch_name, switch_code)

        self.assertIn(switch_name, switch_page.return_result)
        insert_img(self.dr, "根据正确的开关名称查询.jpg")

    def test_query_switch_error_name(self):
        """根据错误的开关名称查询"""

        switch_name = '录音2'
        switch_code = ''
        switch_page = SwitchPage(self.dr)

        switch_page.query_information(switch_name, switch_code)

        self.assertEqual('没有找到匹配的记录', switch_page.null_msg)
        insert_img(self.dr, "根据错误的开关名称查询.jpg")

    def test_query_switch_code(self):
        """根据正确的开关代号查询"""

        switch_name = ''
        switch_code = '10080000'
        switch_page = SwitchPage(self.dr)

        switch_page.query_information(switch_name, switch_code)

        self.assertIn(switch_code, switch_page.return_result)
        insert_img(self.dr, "根据正确的开关代号查询.jpg")

    def test_query_button_error_code(self):
        """根据错误的开关代号查询"""

        switch_name = ''
        switch_code = '100800002'
        switch_page = SwitchPage(self.dr)

        switch_page.query_information(switch_name, switch_code)

        self.assertEqual('没有找到匹配的记录', switch_page.null_msg)
        insert_img(self.dr, "根据错误的开关代号查询.jpg")

    def test_query_name_and_code_error(self):
        """根据错误的开关名称和代号查询"""

        switch_name = '123123'
        switch_code = '100800002'
        switch_page = SwitchPage(self.dr)

        switch_page.query_information(switch_name, switch_code)

        self.assertEqual('没有找到匹配的记录', switch_page.null_msg)
        insert_img(self.dr, "根据错误的开关名称和代号查询.jpg")


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(SwitchCase("test_delete_switch"))
    # # suite.addTest(SwitchCase("test_query_switch_name"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
