import unittest

import time
from selenium import webdriver


class membermanagetest(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        #设置隐式等待
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def tearDown(self):
        #quit()退出整个浏览器
        #close()关闭一个浏览器标签
        #代码编写和调试的时候需要在quit()方法前加一个时间等待
        #正常运行的时候去掉时间等待
        time.sleep(20)
        self.driver.quit()
    def test_add_member(self):
        # self.driver.get("")
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("xiaoxiao")
        driver.find_element_by_name("mobile_phone").send_keys("13959874562")
        driver.find_element_by_css_selector("[value='1']")
        driver.find_element_by_name("birthday").send_keys("2000-11-11")
        driver.find_element_by_name("email").send_keys("595374598@qq.com")
        driver.find_element_by_name("qq").send_keys("595374598")
        driver.find_element_by_class_name("button_search").click()

