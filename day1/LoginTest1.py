#1、打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost")
driver.find_element_by_link_text("登录").click()
cwh = driver.current_window_handle
whs = driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to(item)