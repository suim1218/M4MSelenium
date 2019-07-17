import os


# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)

    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)
    file_path = base_dir + "/image/" + file_name
    # print(file_path)
    driver.get_screenshot_as_file(file_path)


'''
if __name__ == '__main__':
    #driver = webdriver.PhantomJS(executable_path='C:\\driver\\phantomjs')
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(2)
    insert_img(driver, 'baidu.jpg')
    driver.quit()
'''
