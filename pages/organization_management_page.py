from pages.base_page import BasePage
from time import sleep


class OrganizationPage(BasePage):
    @property
    def organization_management_btn(self):
        return self.by_link_text('组织管理')

    @property
    def people_management_btn(self):
        return self.by_link_text('人员管理')

    # 定位到一级J_iframe表单
    def switch_form1(self):
        xp = self.driver.find_element_by_xpath("//div[@id='content-main']/iframe")
        self.driver.switch_to.frame(xp)

    # 定位到二级control-frame表单
    def switch_form2(self):
        sleep(0.4)
        xp = self.driver.find_element_by_xpath("//iframe[@id='control-frame']")
        self.driver.switch_to.frame(xp)

    # 退出一层表单
    def quit_iframe(self):
        self.driver.switch_to.parent_content()

    # 添加组织按钮
    @property
    def add_organization_btn(self):
        return self.by_id('btn-add-org')

    # 修改组织按钮
    @property
    def modify_organization_btn(self):
        return self.by_id('btn-update-org')

    # 删除组织按钮
    @property
    def delete_organization_btn(self):
        return self.by_id('btn-delete-org')

    # 点击根组织
    @property
    def root_organization_btn(self):
        return self.by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/ul/li[1]')

    # 不选择根组织点击添加组织/修改组织/删除组织提示语
    @property
    def not_select_organization_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 组织名称输入框
    @property
    def organization_name_textfield(self):
        return self.by_id('name-save')

    # 组织名称输入框添加按钮
    @property
    def add_btn(self):
        return self.by_id('btn-save')

    # 添加组织成功提示语
    @property
    def add_organization_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 组织名称为空提示语
    @property
    def organization_name_null_msg(self):
        return self.by_xpath('//form[@id="form-save"]/div[2]/small[1]').text

    # 组织名称过长提示语
    @property
    def organization_name_long_msg(self):
        return self.by_xpath('//form[@id="form-save"]/div[2]/small[2]').text

    # 组织名称重复/提示语
    @property
    def organization_name_repeat_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 选择第一个子组织
    @property
    def select_first_child_organization(self):
        return self.by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/ul/li[2]')

    # 确定删除按钮
    @property
    def confirm_delete_btn(self):
        return self.by_class_name('confirm')

    # 删除组织成功提示语
    @property
    def delete_organization_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 修改组织名称输入框
    @property
    def update_organization_textfield(self):
        return self.by_xpath("(//input[@id='name-save'])[2]")

    # 修改组织名称确认按钮
    @property
    def update_organization_btn(self):
        return self.by_id('btn-update')

    # 修改组织名称成功提示语
    @property
    def update_organization_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 不选择组织点击添加按钮
    def not_select_organization_click_add(self):
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        sleep(1)
        self.add_organization_btn.click()
        sleep(1)

    # 不选择组织点击修改按钮
    def not_select_organization_click_modify(self):
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        sleep(1)
        self.modify_organization_btn.click()
        sleep(1)

    # 不选择组织点击删除按钮
    def not_select_organization_click_delete(self):
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        sleep(1)
        self.delete_organization_btn.click()
        sleep(1)

    # 添加组织
    def add_organization(self, organization_name):
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        self.root_organization_btn.click()
        sleep(0.5)
        self.add_organization_btn.click()
        sleep(0.5)
        self.organization_name_textfield.send_keys(organization_name)
        sleep(0.5)
        self.add_btn.click()
        sleep(2)

    # 添加重名组织
    def add_repeat_organization_name(self, organization_name):
        self.add_organization(organization_name)
        self.driver.refresh()
        self.add_organization(organization_name)
        sleep(1.5)

    # 删除组织
    def delete_organization(self, organization_name):
        self.add_organization(organization_name)
        self.driver.refresh()
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        self.select_first_child_organization.click()
        sleep(0.5)
        self.delete_organization_btn.click()
        sleep(1.5)
        self.confirm_delete_btn.click()
        sleep(3)

    # 修改组织
    def modify_organization_name(self, new_organization_name):
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        self.root_organization_btn.click()
        sleep(2)
        self.modify_organization_btn.click()
        sleep(1)
        self.update_organization_textfield.clear()
        sleep(1)
        self.update_organization_textfield.send_keys(new_organization_name)
        sleep(1)
        self.update_organization_btn.click()
        sleep(2)
