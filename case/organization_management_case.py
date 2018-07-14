# coding: utf-8
import unittest
import time
from public.screenshot import insert_img
from case.base_case import BaseCase
from pages.organization_management_page import OrganizationPage


class OrganizationCase(BaseCase):

    # @unittest.skip
    def test_not_select_organization_click_add(self):
        """不选择根组织点击添加组织按钮"""

        organization_page = OrganizationPage(self.dr)
        organization_page.not_select_organization_click_add()
        self.assertEqual('请先选择组织', organization_page.not_select_organization_msg)
        # print(organization_page.not_select_organization_msg)
        insert_img(self.dr, "不选择根组织点击添加组织按钮.jpg")

    def test_not_select_organization_click_modify(self):
        """不选择根组织点击修改组织按钮"""

        organization_page = OrganizationPage(self.dr)
        organization_page.not_select_organization_click_modify()
        self.assertEqual('请先选择组织', organization_page.not_select_organization_msg)
        # print(organization_page.not_select_organization_msg)
        insert_img(self.dr, "不选择根组织点击修改组织按钮.jpg")

    def test_not_select_organization_click_delete(self):
        """不选择根组织点击删除组织按钮"""

        organization_page = OrganizationPage(self.dr)
        organization_page.not_select_organization_click_delete()
        self.assertEqual('请选择组织机构', organization_page.not_select_organization_msg)
        # print(organization_page.not_select_organization_msg)
        insert_img(self.dr, "不选择根组织点击删除组织按钮.jpg")

    def test_add_organization(self):
        """成功添加组织"""

        organization_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        organization_page = OrganizationPage(self.dr)
        organization_page.add_organization(organization_name)
        self.assertIn('操作成功', organization_page.add_organization_success_msg)
        # print(organization_page.add_organization_success_msg)
        insert_img(self.dr, "成功添加组织.jpg")

    def test_organization_name_null(self):
        """组织名称为空"""

        organization_name = ''
        organization_page = OrganizationPage(self.dr)
        organization_page.add_organization(organization_name)
        self.assertEqual('组织名称不能为空', organization_page.organization_name_null_msg)
        # print(organization_page.organization_name_null_msg)
        insert_img(self.dr, "组织名称为空.jpg")

    def test_organization_name_long(self):
        """组织名称过长"""

        organization_name = '很长很长的组织名称很长很长的组织名称很长很长的组织名称很长很长的组织名称很长很长的组织名称很长很长的组织名称'
        organization_page = OrganizationPage(self.dr)
        organization_page.add_organization(organization_name)
        self.assertEqual('长度不超过30位', organization_page.organization_name_long_msg)
        # print(organization_page.organization_name_long_msg)
        insert_img(self.dr, "组织名称过长.jpg")

    def test_organization_name_repeat(self):
        """添加重复的组织名称"""

        organization_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        organization_page = OrganizationPage(self.dr)
        organization_page.add_repeat_organization_name(organization_name)
        self.assertIn('名称已经存在', organization_page.organization_name_repeat_msg)
        # print(organization_page.organization_name_repeat_msg)
        insert_img(self.dr, "添加重复的组织名称.jpg")

    def test_delete_organization(self):
        """删除组织"""

        organization_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        organization_page = OrganizationPage(self.dr)
        organization_page.delete_organization(organization_name)
        self.assertIn('操作成功', organization_page.delete_organization_success_msg)
        # print(organization_page.delete_organization_success_msg)
        insert_img(self.dr, "删除组织.jpg")

    def test_update_organization(self):
        """成功修改组织名称"""

        new_organization_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        organization_page = OrganizationPage(self.dr)
        organization_page.modify_organization_name(new_organization_name)
        self.assertIn('操作成功', organization_page.update_organization_success_msg)
        # print(organization_page.update_organization_success_msg)
        # insert_img(self.dr, "成功修改组织名称.jpg")


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(OrganizationCase("test_organization_name_repeat"))
    # suite.addTest(AddRoleCase("test_add_role_long"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
