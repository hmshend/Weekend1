#1、打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
#2、打开海盗商城首页
driver.get("http://localhost")
#3、点击注册链接
# 第四种元素定位方法：link
driver.find_element_by_link_text("注册").click()
#窗口切换：把selenium切换到新的窗口工作
cwh = driver.current_window_handle    #浏览器当前窗口的句柄
#selenium只提供了selenium工作的窗口的名字，并没有提供第二个窗口的名字（自己求）
whs = driver.window_handles #浏览器中所有的窗口句柄
#for关键字 item表示集合中的某个元素  in关键字   数组/集合
for item in whs:
    if item == cwh:
        driver.close()
    else:  #这种情况就是item要找的窗口
        driver.switch_to.window(item)
#4、输入用户信息
driver.find_element_by_name("username").send_keys("shm211")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("13999999988")
driver.find_element_by_name("email").send_keys("987654333@qq.com")
driver.find_element_by_class_name("reg_btn").click()
#5、点击提交按钮