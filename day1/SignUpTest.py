from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("shm1")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("13999999999")
driver.find_element_by_name("email").send_keys("987654321@qq.com")
driver.find_element_by_class_name("reg_btn").click()
