from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from time import sleep


class BlackPage(BasePage):
    @property
    def security_management_btn(self):
        return self.by_link_text('安全管理')

    @property
    def internet_control_btn(self):
        return self.by_link_text('上网管控')

    # 定位到二级control-frame表单
    def switch_iframe(self):
        xp = self.driver.find_element_by_xpath("//div[@id='content-main']/iframe")
        self.driver.switch_to.frame(xp)
        sleep(0.4)
        xp = self.driver.find_element_by_xpath("//iframe[@id='control-frame']")
        self.driver.switch_to.frame(xp)

    # 退出一层表单
    def quit_iframe(self):
        self.driver.switch_to.parent_content()

    # 主页面添加按钮
    def add_btn(self):
        return self.by_id('btn-add')

    # 添加黑名单名称
    @property
    def blacklist_name(self):
        return self.by_id('name')

    # 添加黑名单网址
    @property
    def blacklist_url(self):
        return self.by_id('url')

    # 添加黑名单界面添加按钮
    @property
    def add2_btn(self):
        return self.by_id('rc-add-btn')

    # 添加黑名单界面取消按钮
    @property
    def cancel_btn(self):
        return self.by_id('rc-add-btn')

    # 添加黑名单成功界面继续添加按钮
    @property
    def add_continue_btn(self):
        return self.by_class_name('confirm')

    # 添加黑名单成功界面返回列表按钮
    @property
    def return_btn(self):
        return self.by_class_name('cancel')

    # 添加黑名单成功提示语
    @property
    def add_black_list_success_msg(self):
        return self.by_xpath('/html/body/div[5]/p').text

    # 黑名单名称为空提示语
    @property
    def black_name_null_msg(self):
        return self.by_xpath("//form[@id='form-ic']/div[1]/small[1]").text

    # 黑名单网址为空提示语
    @property
    def blacklist_url_null_msg(self):
        return self.by_xpath("//form[@id='form-ic']/div[2]/small[1]").text

    # 黑名单名称过长提示语
    @property
    def blacklist_longname_msg(self):
        return self.by_xpath("//form[@id='form-ic']/div[1]/small[2]").text

    # 黑名单URL过长提示语
    @property
    def blacklist_long_url_msg(self):
        return self.by_xpath("//form[@id='form-ic']/div[2]/small[2]").text

    # 第一条上网黑名单的名称
    @property
    def first_row(self):
        return self.by_xpath("//table[@id='dataTable']/tbody/tr[1]/td[2]")

    # 下发策略按钮
    @property
    def develop_btn(self):
        return self.by_id("btn-send")

    # 下发策略后确定按钮
    @property
    def develop_confirm_btn(self):
        return self.by_class_name("confirm")

    # 下发策略后再次确定按钮
    @property
    def develop_continue_confirm_btn(self):
        return self.by_class_name("confirm")

    # 下发策略成功提示
    @property
    def develop_success_msg(self):
        return self.by_xpath("/html/body/div[3]/p").text

    # 批量导入按钮
    @property
    def import_blacklist_btn(self):
        return self.by_id("btn-import")

    # 上传黑名单文件
    @property
    def upload_files_btn(self):
        return self.by_id("import-user-file")

    # 上传黑名单文件后点击uplocad按钮
    @property
    def upload_btn(self):
        return self.by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/form/div/div[2]/div[2]/a/span")

    # 上传黑名单文件成功提示语
    @property
    def upload_files_success_msg(self):
        return self.by_xpath("/html/body/div[5]/p").text

    # 上传黑名单文件第一行为空提示语
    @property
    def upload_files_success_msg(self):
        return self.by_xpath("/html/body/div[5]/p").text

    # 删除黑名单按钮
    @property
    def delete_btn(self):
        return self.by_id("btn-delete")

    # 选择第一行黑名单
    @property
    def select_first_blacklist(self):
        return self.by_xpath("//table[@id='dataTable']/tbody/tr[1]/td[1]/input")

    # 添加或者删除黑名单后选择所有黑名单
    @property
    def select_all_blacklist(self):
        return self.by_xpath(
            "/html/body/div[1]/div/div/div/div/div[4]/div[1]/div[2]/div[2]/table/thead/tr/th[1]/div[1]/input")

    # 确定删除按钮
    @property
    def delete_confirm_btn(self):
        return self.by_class_name("confirm")

    # 黑名单列表页为空提示信息
    @property
    def blacklist_null_msg(self):
        return self.by_xpath("//table[@id='dataTable']/tbody/tr[1]/td").text

    # 添加黑名单
    def add_black_list(self, black_list_name, black_list_url):
        self.security_management_btn.click()
        self.internet_control_btn.click()
        self.switch_iframe()
        self.add_btn().click()
        self.blacklist_name.send_keys(black_list_name)
        sleep(0.5)
        self.blacklist_url.send_keys(black_list_url)
        sleep(0.5)
        self.add2_btn.click()
        sleep(1)

    # 继续添加黑名单
    def continue_add_black_list(self, black_list_name, black_list_url):
        self.add_continue_btn.click()
        self.blacklist_name.send_keys(black_list_name)
        sleep(0.5)
        self.blacklist_url.send_keys(black_list_url)
        sleep(0.5)
        self.add2_btn.click()
        sleep(1)

    # 下发黑名单策略
    def develop_black_list(self):
        self.security_management_btn.click()
        self.internet_control_btn.click()
        self.switch_iframe()
        self.develop_btn.click()
        sleep(1)
        self.develop_confirm_btn.click()
        sleep(1)
        self.develop_continue_confirm_btn.click()
        sleep(1)

    # 导入黑名单
    def import_black_list(self, file):
        self.security_management_btn.click()
        self.internet_control_btn.click()
        self.switch_iframe()
        self.import_blacklist_btn.click()
        self.upload_files_btn.send_keys(file)
        self.upload_btn.click()
        sleep(1.5)

    # 删除第一行黑名单
    def delete_first_row_black_list(self):
        self.select_first_blacklist.click()
        self.delete_btn.click()
        sleep(0.5)
        self.delete_confirm_btn.click()
        sleep(1.5)

    # 删除第一页黑名单
    def delete_first_page_black_list(self):
        self.select_all_blacklist.click()
        sleep(1.5)
        self.delete_btn.click()
        sleep(0.5)
        self.delete_confirm_btn.click()
        sleep(1.5)
