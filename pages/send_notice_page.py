from pages.base_page import BasePage
from time import sleep


class NoticePage(BasePage):
    @property
    def things_management_btn(self):
        return self.by_link_text('事务管理')

    @property
    def message_push_btn(self):
        return self.by_link_text('消息推送')

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

    # 点击公告按钮
    @property
    def notice_btn(self):
        return self.by_link_text('公告')

    # 点击新建公告按钮
    @property
    def add_notice_btn(self):
        return self.by_id('btn-add')

    # 选择管理部门
    @property
    def root_tissue_btn(self):
        return self.by_xpath('/html/body/div/div/div[2]/div[1]/div[2]/div/ul/li[1]/span[3]')

    # 消息内容输入框
    @property
    def addressee_textfield(self):
        return self.by_id('notice-text')

    # 发送按钮
    @property
    def send_btn(self):
        return self.by_id('save-btn')

    # 确定发送按钮
    @property
    def send_confirm_btn(self):
        return self.by_class_name('confirm')

    # 收件人为空提示语
    @property
    def address_null_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 消息内容过长提示语
    @property
    def notice_long_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 消息发送成功提示语
    @property
    def send_notice_success_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 使发送公告提示语可见
    @property
    def send_notice_success_msg(self):
        return self.driver.execute_script("return $('.sweet-alert p').text()")

    # 点击取消按钮提示语
    @property
    def cancel_send_notice_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 选择管理部门发送公告
    def select_management_send_notice(self, message):
        self.things_management_btn.click()
        self.message_push_btn.click()
        sleep(0.5)
        self.switch_form1()
        self.notice_btn.click()
        sleep(0.5)
        self.switch_form2()
        self.add_notice_btn.click()
        sleep(0.5)
        self.root_tissue_btn.click()
        self.addressee_textfield.send_keys(message)
        sleep(0.5)
        self.send_btn.click()
        sleep(0.5)
        self.send_confirm_btn.click()
        sleep(0.5)

    # 选择管理部门发送公告
    def null_management_send_notice(self, message):
        self.things_management_btn.click()
        self.message_push_btn.click()
        sleep(0.5)
        self.switch_form1()
        self.notice_btn.click()
        sleep(0.5)
        self.switch_form2()
        self.add_notice_btn.click()
        sleep(0.5)
        self.addressee_textfield.send_keys(message)
        sleep(0.5)
        self.send_btn.click()
        sleep(0.5)
        self.send_confirm_btn.click()
        sleep(0.5)
