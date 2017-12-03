#1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("shm")
#Chains链表和数组不同，数组有固定的长度，链表必须有明确的结束标志
#perform执行
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
#3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
#4.修改个人信息
#更好的编程习惯是，在每次执行sendkeys前，都进行一边clear操作
#4a真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("你好呀")
#4b.性别
driver.find_element_by_css_selector("#xb[value='2']").click()
#javascript是一个单独语言，和python语法不一样，不能直接在pycharm中执行
# js = 'Document.find_element_by_id("date").removeAttribute("readonly")'
# driver.execute_script(js) #执行js脚本
# driver.find_element_by_id("date").clear()
# driver.find_element_by_id("date").send_keys("2001-11-21")
#用arguments改写上面输入
#用arguments改写上面输入，用selenium定位方式，定位元素之后，对元素执行javascript脚本，删除readonly
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("1980-11-22")
#return把javascript的执行结果返回给python
# date = driver.execute_script("return Document.find_element_by_id('date')")
# date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("595374589")
driver.find_element_by_class_name("btn4").click()
#右键检查不了的弹出框，叫做alert，有单独的方法来处理
time.sleep(3)
#alert控件不是html代码生成的，所以implicitly_wait对这个控件不管用
driver.switch_to.alert.accept()


