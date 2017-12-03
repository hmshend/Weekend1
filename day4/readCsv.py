#1、导入csv包
import csv
#2、要想读取文件的信息，首先要知道文件的存放路径
path = r"C:\Users\51Testing\PycharmProjects\Weekend1\data\member_info.csv"
#3、要想读文件内容，首先要通过路径打开文件
file = open(path,'r')
#4、通过csv代码库，读取csv格式的内容
data_table = csv.reader(file)
#5、遍历data_table，分别打印每一行数据
for row in data_table:
    print(row)