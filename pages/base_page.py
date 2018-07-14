class BasePage(object):
    url = None
    driver = None
    domain = None

    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.get_title()

    def url(self):
        return self.url

    def navigate(self):
        self.driver.get(self.url)

    def by_id(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.driver.find_element_by_name(the_name)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def js(self, js_text):
        return self.driver.execute_script(js_text)

    def by_link_text(self, the_link_text):
        return self.driver.find_element_by_link_text(the_link_text)

    def by_xpath(self, the_xpath):
        return self.driver.find_element_by_xpath(the_xpath)

    def by_class_name(self, the_class_name):
        return self.driver.find_element_by_class_name(the_class_name)

    def by_tag_name(self, the_tag_name):
        return self.driver.find_element_by_tag_name(the_tag_name)
