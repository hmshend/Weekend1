#1、打开浏览器
from selenium import webdriver
#从selenium导入webdriver网络驱动，用代码来操作浏览器
#python语言不需要加分号
#第二个Chrome后面一定要加括号
driver = webdriver.Chrome()
#2、打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3、输入用户名
driver.find_element_by_id("username").send_keys("shm")
#4、输入密码
driver.find_element_by_id("password").send_keys("123456")
#5、点击登录按钮
driver.find_element_by_class_name("login_btn").click()