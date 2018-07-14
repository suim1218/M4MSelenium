# coding: utf-8
import unittest
import time
from case.base_case import BaseCase
from public.screenshot import insert_img
from pages.people_management_page import PeoplePage


class PeopleCase(BaseCase):

    # @unittest.skip
    def test_add_people(self):
        """添加人员成功"""
        name = time.strftime("%Y_%m_%d_%H_%M_%S")
        phone = '13111111111'

        people_page = PeoplePage(self.dr)
        people_page.add_people(name, phone)
        # self.assertEqual('请先选择组织', organization_page.not_select_organization_msg)
        # print(organization_page.not_select_organization_msg)
        # people_page.edit_people(name)
        # insert_img(self.dr, "不选择根组织点击添加组织按钮.jpg")


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(PeopleCase("test_add_people"))
    # suite.addTest(PeopleCase("test_add_role_long"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
