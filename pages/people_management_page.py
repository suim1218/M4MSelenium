from pages.base_page import BasePage
from time import sleep


class PeoplePage(BasePage):
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

    # 点击根组织
    @property
    def root_organization_btn(self):
        return self.by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/ul/li[1]')

    # 添加人员按钮
    @property
    def add_people_btn(self):
        return self.by_id('btn-add')

    # 姓名输入框
    @property
    def people_name_textfield(self):
        return self.by_xpath('//form[@id="form-user"]/div[1]/input')

    # 手机号码输入框
    @property
    def people_phone_textfield(self):
        return self.by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/div[1]/form/div[3]/input')

    # 添加用户信息界面添加按钮
    @property
    def add_btn(self):
        return self.by_id('user-add-btn')

    # 找到刚刚添加的联系人 并点击编辑
    def edit_people(self, a):
        return self.driver.execute_script(
            '$("tr").each(function(){if($(this).find("td:nth-child(2)").text() == "' + a + '" ){$(this).find("td:nth-child(2)").parent().find(".like").trigger("click")}})')

    def add_people(self, name, phone):
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        self.root_organization_btn.click()
        sleep(1)
        self.add_people_btn.click()
        sleep(2)
        self.people_name_textfield.send_keys(name)
        sleep(5)
        # self.people_phone_textfield(phone)
        # sleep(1)
        self.add_btn.click()
        sleep(1)
        self.driver.refresh()
        self.organization_management_btn.click()
        self.people_management_btn.click()
        self.switch_form1()
        sleep(5)
        self.root_organization_btn.click()
        sleep(10)
        self.edit_people(name)
        sleep(5)
