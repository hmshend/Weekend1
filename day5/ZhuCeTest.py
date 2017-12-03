#有了myTestCase以后，再写测试用例，就不需要重新写setup和tearDown方法了
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    #三个双引号，表示文档字符串，也是一种注释，和#的区别是3个双引号会显示在文档里面
    """注册模块测试用例"""
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.current_url #用来获取当前浏览器中的网址
        actual = driver.title #用来获取当前浏览器中的标签页的title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        #get_screenshot_as_file截取浏览器的图片
        base_path = os.path.dirname(__file__)
        path=base_path.replace('day5','report/image/')
        driver.get_screenshot_as_file(path + "zhuce.png")
        self.assertEqual(actual,expected)