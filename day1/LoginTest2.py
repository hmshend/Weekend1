#javascript是一门独立的语言
#要想学好selenium，最重要的三件事：
#1、元素的定位：id--->name--->class
#link_text必须是链接，必须是<a>标签，
#2、元素的操作：鼠标左键单机click，发送键盘上的按键send_keys
#3、学好javascript
#用javascript实现窗口切换
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost")
#javascript和python是不同的语言，pycharm是用来写python语言
#怎么在python执行javascript语言
js = "document.getElementsByClassName('site-nav-right fr')[0].childNodes[1].removeAttribute('target')"
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
#3、输入用户名
driver.find_element_by_id("username").send_keys("shm")
#4、输入密码
driver.find_element_by_id("password").send_keys("123456")
#5、点击登录按钮
driver.find_element_by_class_name("login_btn").click()
time.sleep(5)
#点击返回商城的链接

# driver.quit()