from pages.base_page import BasePage


class DashboardPage(BasePage):
    @property
    def greeting_link(self):
        return self.by_id('logout-a')

    @property
    def welcome_msg(self):
        return self.greeting_link.text
