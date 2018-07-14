from pages.base_page import BasePage
from time import sleep


class ModifyPasswordPage(BasePage):
    @property
    def system_settings_btn(self):
        return self.by_link_text('系统设置')

    @property
    def modify_password_btn(self):
        return self.by_link_text('修改密码')

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

    # 原密码输入框
    @property
    def old_password_textfield(self):
        return self.by_id('code0')

    # 新密码输入框
    @property
    def new_password_textfield(self):
        return self.by_id('code1')

    # 新密码第二次输入
    @property
    def new_password_again_textfield(self):
        return self.by_id('code2')

    # 确认修改按钮
    @property
    def confirm_modify_btn(self):
        return self.by_id('btn-update')

    # 原密码为空提示语
    @property
    def old_password_null_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div[1]/small[1]').text

    # 新密码为空提示语
    @property
    def new_password_null_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div[2]/small[1]').text

    # 新密码过长提示语
    @property
    def new_password_long_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div[2]/small[2]').text

    # 新密码过短提示语
    @property
    def new_password_short_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div[2]/small[2]').text

    # 确认新密码输入框为空提示语
    @property
    def new_password_again_null_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div[3]/small[1]').text

    # 两次密码输入不一致提示语
    @property
    def different_password_msg(self):
        return self.by_xpath('//form[@id="form-app"]/div[3]/small[4]').text

    # 新密码只为一种字符提示语
    @property
    def new_password_one_type(self):
        return self.by_xpath('//form[@id="form-app"]/div[2]/small[3]').text

    # 修改密码成功提示语
    @property
    def modify_password_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    def modify_password(self, old_password, new_password, again_password):
        self.system_settings_btn.click()
        self.modify_password_btn.click()
        self.switch_form1()
        self.old_password_textfield.send_keys(old_password)
        sleep(0.5)
        self.new_password_textfield.send_keys(new_password)
        sleep(0.5)
        self.new_password_again_textfield.send_keys(again_password)
        sleep(0.5)
        self.confirm_modify_btn.click()
        sleep(1)
