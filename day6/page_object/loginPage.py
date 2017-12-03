from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    title = "我的会员中心 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"
    #小括号表示元组，元组中有两个元素，第一个元素是控件的定位方式
    #第二个元素，控件定位方式的具体值
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()
    def open(self):
        self.driver.get(self.url)
    def input_username(self,username):
        #星号的作用就是把一个元祖中的元素分别传入方法参数中
        #前面加一个星号，表示传入就不是元组，而是元祖中的两个元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
