#测试框架是干什么用的
#最主要的用途是组织和执行测试用例
#1、导入unittest框架
import unittest
#2.继承unittest中的父类
#python中的继承直接用小括号表示
class unittestdemo(unittest.TestCase):
    def setUp(self):
        print("这个方法将会在测试用例执行前先执行")
    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")
#编写测试用例方法
    #只有以test开头命名的方法才是测试用例的方法
    #测试用例方法，可以直接被运行
    #普通方法不能直接运行，只有被调用时才能执行
    def test_log_in(self):
        print("登录测试用例")
        self.zhu_ce()

    def zhu_ce(self):
        print("注册测试用例")
    def test_search(self):
        print("搜索测试用例")
#如果你直接执行这个文件，那么就会执行下面的语句
#否则，你执行其他文件，import这个文件的时候，下面的代码就不会被执行
if __name__ == '__main__':
    #执行当前文件中所有的unittest的测试用例
    # unittest.main()
    unittestdemo().zhu_ce()