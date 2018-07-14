from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.select import Select


class ButtonPage(BasePage):
    @property
    def system_maintenance_btn(self):
        return self.by_link_text('系统维护')

    @property
    def button_btn(self):
        return self.by_link_text('按钮')

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

    # 点击添加按钮
    @property
    def add_button_btn(self):
        return self.by_id('btn-add')

    # 操作名称输入框
    @property
    def button_name_textfield(self):
        return self.by_name('name')

    # 操作编码输入框
    @property
    def button_code_textfield(self):
        return self.by_name('code')

    # 保存按钮
    @property
    def save_btn(self):
        return self.by_id('btn-save')

    # 操作名称为空提示语
    @property
    def button_name_null_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div/div[1]/small[1]').text

    # 操作名称过长提示语
    @property
    def button_name_long_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div/div[1]/small[2]').text

    # 操作编码为空提示语
    @property
    def button_code_null_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div/div[2]/small[1]').text

    # 操作编码过长提示语
    @property
    def button_code_long_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div/div[2]/small[2]').text

    # 操作编码重复提示语
    @property
    def button_code_repeat_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div/div[2]/small[3]').text

    # 添加按钮成功提示语
    @property
    def add_button_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 返回查询结果
    @property
    def return_result(self):
        a = self.by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div[2]/div[2]/table/tbody/tr').text
        b = a.split(' ')
        return b

    # 删除按钮
    @property
    def delete_switch_btn(self):
        return self.by_xpath('//table[@id="operationTable"]/tbody/tr[1]/td[3]/span/span/a/span')

    # 确定删除按钮
    @property
    def delete_confirm_btn(self):
        return self.by_class_name('confirm')

    # 删除成功提示语
    @property
    def delete_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 无匹配记录提示语
    @property
    def null_msg(self):
        return self.by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td').text

    # 编辑按钮
    @property
    def edit_btn(self):
        return self.by_xpath('//table[@id="operationTable"]/tbody/tr[1]/td[3]/a/span')

    # 搜索名称输入框
    @property
    def query_button_name_textfield(self):
        return self.by_id('operationName')

    # 搜索编码输入框
    @property
    def query_button_code_textfield(self):
        return self.by_id('code')

    # 查询按钮
    @property
    def query_btn(self):
        return self.by_id('btn-query')

    # 添加开关
    def add_button(self, button_name, button_code):
        self.system_maintenance_btn.click()
        self.button_btn.click()
        self.switch_form1()
        self.add_button_btn.click()
        self.button_name_textfield.send_keys(button_name)
        sleep(1)
        self.button_code_textfield.send_keys(button_code)
        self.save_btn.click()
        sleep(2)

    # 查询
    def query_information(self, button_name, button_code):
        self.system_maintenance_btn.click()
        self.button_btn.click()
        self.switch_form1()
        self.query_button_name_textfield.send_keys(button_name)
        self.query_button_code_textfield.send_keys(button_code)
        sleep(2)
        self.query_btn.click()
        sleep(1)
