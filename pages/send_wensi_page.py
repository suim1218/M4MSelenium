from pages.base_page import BasePage
from time import sleep


class WensiPage(BasePage):
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

    # 定位到三级表单
    def switch_form3(self):
        sleep(0.4)
        xp = self.driver.find_element_by_xpath("//div[@id='edui1_iframeholder']/iframe")
        self.driver.switch_to.frame(xp)

    # 退出一层表单
    def quit_iframe(self):
        self.driver.switch_to.parent_frame()

    # 点击闻思按钮
    @property
    def wensi_btn(self):
        return self.by_link_text('闻思')

    # 点击新建闻思按钮
    @property
    def add_wensi_btn(self):
        return self.by_id('btn-add')

    # 标题输入框
    @property
    def title_textfield(self):
        return self.by_id('title')

    # 内容输入框
    @property
    def content_textfield(self):
        return self.by_tag_name('body')

    # 保存按钮
    @property
    def save_btn(self):
        return self.by_xpath('//*[@id="save-btn"]')

    # 发布按钮
    @property
    def send_btn(self):
        return self.by_xpath('//*[@id="send-btn"]')

    # 闻思标题或内容为空提示语
    @property
    def wensi_title_or_content_null_msg(self):
        return self.by_xpath('/html/body/div[5]/p').text

    # 闻思标题过长提示语
    @property
    def wensi_title_long_msg(self):
        return self.by_xpath('/html/body/div[5]/p').text

    # 返回发送人、发送日期、发送时间、发布状态、继续编辑
    @property
    def return_result(self):
        a = self.by_xpath('/html/body/div/div/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]').text
        b = a.split(' ')
        return b

    # 返回闻思描述
    @property
    def return_describe(self):
        a = self.by_xpath('/html/body/div/div/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/span[1]').text
        return a

    # 编辑按钮
    @property
    def edit_btn(self):
        return self.by_xpath('//table[@id="newsTable"]/tbody/tr[1]/td[6]/a/span')

    # 删除按钮
    @property
    def delete_btn(self):
        return self.by_xpath('//table[@id="newsTable"]/tbody/tr[1]/td[6]/span/a[2]/span')

    # 确认删除按钮
    @property
    def confirm_btn(self):
        return self.by_class_name('confirm')

    # 删除成功提示语
    @property
    def delete_success_msg(self):
        return self.by_xpath('/html/body/div[3]/p').text

    # 发送闻思
    def send_wensi(self, title, content):
        self.things_management_btn.click()
        self.message_push_btn.click()
        sleep(0.5)
        self.switch_form1()
        self.wensi_btn.click()
        sleep(0.5)
        self.switch_form2()
        self.add_wensi_btn.click()
        sleep(0.5)
        self.title_textfield.send_keys(title)
        sleep(1)
        self.switch_form3()
        self.content_textfield.send_keys(content)
        sleep(1)
        self.quit_iframe()
        self.save_btn.click()
        sleep(4)
        self.send_btn.click()
        self.quit_iframe()
        self.wensi_btn.click()
        sleep(2)
        self.switch_form2()

    # 保存闻思
    def save_wensi(self, title, content):
        self.things_management_btn.click()
        self.message_push_btn.click()
        sleep(0.5)
        self.switch_form1()
        self.wensi_btn.click()
        sleep(0.5)
        self.switch_form2()
        self.add_wensi_btn.click()
        sleep(0.5)
        self.title_textfield.send_keys(title)
        sleep(1)
        self.switch_form3()
        self.content_textfield.send_keys(content)
        sleep(1)
        self.quit_iframe()
        self.save_btn.click()

    # 保存闻思后返回列表页
    def save_wensi_and_return(self, title, content):
        self.save_wensi(title, content)
        self.quit_iframe()
        self.wensi_btn.click()
        sleep(2)
        self.switch_form2()

    # 发送闻思后编辑
    def edit_wensi(self, title, content, new_title, new_content):
        self.send_wensi(title, content)
        self.edit_btn.click()
        sleep(1)
        self.title_textfield.clear()
        self.title_textfield.send_keys(new_title)
        sleep(1)
        self.switch_form3()
        self.content_textfield.clear()
        self.content_textfield.send_keys(new_content)
        sleep(1)
        self.quit_iframe()
        self.save_btn.click()
        sleep(1)
        self.quit_iframe()
        self.wensi_btn.click()
        sleep(2)
        self.switch_form2()

    # 发送闻思后删除
    def delete_wensi(self, title, content):
        self.send_wensi(title, content)
        self.delete_btn.click()
        sleep(1)
        self.confirm_btn.click()
