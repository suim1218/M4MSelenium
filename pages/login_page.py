from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    @property
    def username_textfield(self):
        return self.by_name('account')

    @property
    def password_textfield(self):
        return self.by_name('pwd')

    @property
    def code_textfield(self):
        return self.by_id('checkImg')

    @property
    def login_btn(self):
        return self.by_id('login-btn')

    @property
    def login_error(self):
        return self.by_css('html body.stop-scrolling div.sweet-alert.showSweetAlert.visible p')

    @property
    def error_msg(self):
        return self.login_error.text

    def login(self, username, password):
        self.username_textfield.clear()
        self.username_textfield.send_keys(username)
        self.password_textfield.clear()
        self.password_textfield.send_keys(password)
        self.code_textfield.send_keys('1111')
        self.login_btn.click()
        return DashboardPage(self.driver)

    def login_success(self):
        self.username_textfield.clear()
        self.username_textfield.send_keys('admin')
        self.password_textfield.clear()
        self.password_textfield.send_keys('Admin123')
        self.code_textfield.send_keys('1111')
        self.login_btn.click()
