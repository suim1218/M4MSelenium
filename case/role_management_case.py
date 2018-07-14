# coding: utf-8
import unittest
import time
from public.screenshot import insert_img
from case.base_case import BaseCase
from pages.role_management_page import RolePage


class AddRoleCase(BaseCase):

    # @unittest.skip
    def test_add_role_success(self):
        """添加角色成功"""

        rolename = time.strftime("%Y_%m_%d_%H_%M_%S")
        role_management_page = RolePage(self.dr)
        role_management_page.add_role(rolename)
        self.assertEqual('操作成功', role_management_page.success_msg)
        # print(role_management_page.success_msg)
        insert_img(self.dr, "添加角色成功.jpg")

    def test_add_role_null(self):
        """角色名称为空"""

        rolename = ''
        role_management_page = RolePage(self.dr)
        role_management_page.add_role(rolename)

        self.assertEqual('名称不能为空', role_management_page.role_null_msg)
        # print(role_management_page.role_null_msg)
        insert_img(self.dr, "角色名称为空.jpg")

    def test_add_role_long(self):
        """角色名称过长"""

        rolename = '角色名称过长角色名称过长角色名称过长角色名称过长角色名称过长2'
        role_management_page = RolePage(self.dr)
        role_management_page.add_role(rolename)

        self.assertEqual('长度不超过30位', role_management_page.role_long_msg)
        # print(role_management_page.role_null_msg)
        insert_img(self.dr, "角色名称过长.jpg")


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(AddRoleCase("test_add_role_null"))
    # suite.addTest(AddRoleCase("test_add_role_long"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
