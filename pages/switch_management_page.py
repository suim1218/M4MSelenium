from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.select import Select


class SwitchPage(BasePage):
    @property
    def system_maintenance_btn(self):
        return self.by_link_text('系统维护')

    @property
    def switch_management_btn(self):
        return self.by_link_text('远程控制开关管理')

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

    # 点击添加开关按钮
    @property
    def add_switch_btn(self):
        return self.by_id('btn-add')

    # 开关名称输入框
    @property
    def switch_name_textfield(self):
        return self.by_name('name')

    # 开关编码输入框
    @property
    def switch_key_textfield(self):
        return self.by_name('key')

    # 开关代号输入框
    @property
    def switch_code_textfield(self):
        return self.by_name('code')

    # 开关类型下拉框选择-------设备开关
    @property
    def select_switch_type1(self):
        sel = self.by_name('type')
        return Select(sel).select_by_value('1')

    # 开关类型下拉框选择-------管控开关
    # @property
    def select_switch_type2(self):
        sel = self.by_name('type')
        return Select(sel).select_by_value('2')

    # 添加按钮
    @property
    def add2_btn(self):
        return self.by_id('rc-add-btn')

    # 取消按钮
    @property
    def cancel_btn(self):
        return self.by_id('rc-cancel-btn')

    # 名称为空提示语
    @property
    def switch_name_null_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[1]/small[1]').text

    # 名称过长提示语
    @property
    def switch_name_long_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[1]/small[2]').text

    # 编码为空提示语
    @property
    def switch_key_null_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[2]/small[1]').text

    # 编码过长提示语
    @property
    def switch_key_long_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[2]/small[3]').text

    # 开关编码重复提示语
    @property
    def switch_key_repeat_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[2]/small[2]').text

    # 开关代号为空提示语
    @property
    def switch_code_null_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[3]/small[1]').text

    # 开关代号过长提示语
    @property
    def switch_code_long_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[3]/small[3]').text

    # 开关代号重复提示语
    @property
    def switch_code_repeat_msg(self):
        return self.by_xpath('//form[@id = "form-rc"]/div[3]/small[2]').text

    # 添加开关成功提示语
    @property
    def add_switch_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 选择第一个开关
    @property
    def select_first_switch(self):
        return self.by_xpath('//table[@id="rcTable"]/tbody/tr[1]/td[1]/input')

    # 删除开关
    @property
    def delete_switch_btn(self):
        return self.by_xpath('//table[@id="rcTable"]/tbody/tr[1]/td[6]/span/span/a/span')

    # 确定删除按钮
    @property
    def delete_confirm_btn(self):
        return self.by_class_name('confirm')

    # 删除成功提示语
    @property
    def delete_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 编辑按钮
    @property
    def edit_btn(self):
        return self.by_xpath('//table[@id="rcTable"]/tbody/tr[1]/td[6]/a/span')

    # 修改按钮
    @property
    def modify_btn(self):
        return self.by_id('rc-update-btn')

    # 搜索名称输入框
    @property
    def query_switch_name_textfield(self):
        return self.by_id('rcName')

    # 搜索开关代号输入框
    @property
    def query_switch_code_textfield(self):
        return self.by_id('rcCode')

    # 查询按钮
    @property
    def query_btn(self):
        return self.by_id('btn-query')

    # 返回查询结果
    @property
    def return_result(self):
        a = self.by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div[2]/div[2]/table/tbody/tr').text
        b = a.split(' ')
        return b

    # 无匹配记录提示语
    @property
    def null_msg(self):
        return self.by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td').text

    # 添加开关
    def add_switch(self, switch_name, switch_key, switch_code):
        self.system_maintenance_btn.click()
        self.switch_management_btn.click()
        self.switch_form1()
        sleep(1)
        self.add_switch_btn.click()
        self.switch_name_textfield.send_keys(switch_name)
        self.switch_key_textfield.send_keys(switch_key)
        self.switch_code_textfield.send_keys(switch_code)
        self.add2_btn.click()
        sleep(3)

    # 添加开关后删除
    def delete_switch(self):
        # self.select_first_switch.click()
        self.delete_switch_btn.click()
        sleep(1)
        self.delete_confirm_btn.click()
        sleep(2)

    # 添加开关后编辑
    def edit_switch(self, new_switch_name, new_switch_key, new_switch_code):
        self.select_first_switch.click()
        self.edit_btn.click()
        self.switch_name_textfield.clear()
        self.switch_name_textfield.send_keys(new_switch_name)
        self.switch_key_textfield.clear()
        self.switch_key_textfield.send_keys(new_switch_key)
        self.switch_code_textfield.clear()
        self.switch_code_textfield.send_keys(new_switch_code)
        self.modify_btn.click()
        sleep(2)

        # 获取所有开关信息
        # @property
        # def get_switch_information(self):
        #     self.by_link_text('系统维护').click()
        #     self.by_link_text('远程控制开关管理').click()
        #     self.switch_form1()
        #     FileList = []
        #     a = self.by_xpath('/html/body/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[2]/table/tbody').text
        #     FileList.append(a)
        #     self.driver.refresh()
        #     sleep(1)
        #     return FileList

        # sleep(2)

    # 查询
    def query_information(self, switch_name, switch_code):
        self.system_maintenance_btn.click()
        self.switch_management_btn.click()
        self.switch_form1()
        self.query_switch_name_textfield.send_keys(switch_name)
        self.query_switch_code_textfield.send_keys(switch_code)
        sleep(2)
        self.query_btn.click()
        sleep(1)

    # 选择开关类型为管控开关
    def select_switch_type(self, switch_name, switch_key, switch_code):
        self.system_maintenance_btn.click()
        self.switch_management_btn.click()
        self.switch_form1()
        sleep(1)
        self.add_switch_btn.click()
        self.switch_name_textfield.send_keys(switch_name)
        self.switch_key_textfield.send_keys(switch_key)
        self.switch_code_textfield.send_keys(switch_code)
        self.select_switch_type2()
        self.add2_btn.click()
        sleep(3)
