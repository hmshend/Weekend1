import os
import smtplib
import unittest
#HTMLTestRunner是基于unittest框架的一个扩展，可以自己在网上自行下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,'rb')
    mail_body = f.read()
    f.close()
    #要想发邮件，我们要把二进制的内容转成MIME格式
    #MIME multipurse多用途 Internet互联网 Mail邮件 Extension扩展
    #MIME是对邮件协议的一个扩展，使邮件不仅支持文本，还支持多种格式，比如图片，音频二进制文件等
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = 'shen11huiming@123.com'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("bwftest126@126.com", "abc123asd654")
    smtp.sendmail('bwftest126@126.com','shen11huiming@126.com', msg.as_string(), mail_options=[], rcpt_options=[])
    print("dsb")
if __name__ == '__main__':
    # str是String f是format格式
    # strftime()通过这个方法可以定义时间的格式
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./day5','*Test.py')
    #文本测试用例运行期
    # unittest.TextTestRunner().run(suite)
    #现在用html的测试用例运行器
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path,'wb')
    HTMLTestRunner(stream=file,title="海盗商城测试报告",description="测试环境：window server 2008 + Chrome").run(suite)
    #我们要把html报告作为邮件正文，发邮件
    file.close()
    send_mail(path)
