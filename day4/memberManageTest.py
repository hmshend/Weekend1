import unittest
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read
#用ddt装饰这个类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #调用之前写好的read()方法，获取配置文件中的数据
    member_info = read("member_info.csv")
    # global driver
    @classmethod
    def setUpClass(cls):
        print("所有方法之前执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def testa_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
    #python中的集合前面的星号表示，表示把集合中的所有元素拆开，一个一个写
#   list=["小红","小明"]
#   *list="小红","小明"
    #@ddt.data()测试数据来源于read()方法
    #把数据表中的每一行传入方法，在方法中增加一个参数row
    @ddt.data(*member_info)
    def testb_add_member(self,row):
        driver = self.driver
    #for循环不太好，推荐使用ddt装饰器，去修饰这个方法，达到每条测试用例独立执行的目的
    #ddt是数据驱动测试 data driver test
    #注释掉for循环，改变代码的缩进 shift+tab  使方法中的代码比方法声明缩进4个空格
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector("[value='" + row[2] + "']").click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        expected = row[0]
        # if actual == expected:
        #     print("测试通过")
        # else:
        #     print("测试失败")
        # driver.find_element_by_class_name("button_search").click()

        # 切换到父框架
        driver.switch_to.parent_frame()
        self.assertEqual(actual, expected)
            # 切换到网页的根节点
            # driver.switch_to.default_content()
if __name__ == '__main__':
    unittest.main()