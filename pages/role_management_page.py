from pages.base_page import BasePage
from time import sleep


class RolePage(BasePage):
    @property
    def address_book_management_btn(self):
        return self.by_link_text('组织管理')

    @property
    def role_management_btn(self):
        return self.by_link_text('角色管理')

    # 定位到一级J_iframe表单
    def switch_form1(self):
        xp = self.driver.find_element_by_xpath("//div[@id='content-main']/iframe")
        self.driver.switch_to.frame(xp)

    # 定位到二级control-frame表单
    def switch_form2(self):
        xp = self.driver.find_element_by_xpath("//div[@id='content-main']/iframe")
        self.driver.switch_to.frame(xp)
        sleep(0.4)
        xp = self.driver.find_element_by_xpath("//iframe[@id='control-frame']")
        self.driver.switch_to.frame(xp)

    # 退出一层表单
    def quit_iframe(self):
        self.driver.switch_to.parent_content()

    # 添加角色按钮
    @property
    def add_role_btn(self):
        return self.by_id('btn-add')

    # 角色名称输入框
    @property
    def role_name_textfield(self):
        return self.by_id('name')

    # 角色名称界面添加按钮
    @property
    def add_btn(self):
        return self.by_id('btn-save')

    # 添加角色名称成功提示语
    @property
    def success_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 添加角色名称为空提示语
    @property
    def role_null_msg(self):
        return self.by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div/form/div/div/small[1]').text

    # 添加角色名称过长提示语
    @property
    def role_long_msg(self):
        return self.by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div/form/div/div/small[3]').text

    # 添加角色
    def add_role(self, rolename):
        self.address_book_management_btn.click()
        self.role_management_btn.click()
        self.switch_form1()
        sleep(1.5)
        self.add_role_btn.click()
        sleep(1.5)
        self.role_name_textfield.send_keys(rolename)
        sleep(1.5)
        self.add_btn.click()
        sleep(2)
