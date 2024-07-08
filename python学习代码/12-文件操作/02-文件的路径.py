# open 参数介绍
# file:用来指定打开的文件（不是文件的名字，而是文件的路径）
# mode：打开文件的模式，默认是 r 表示只读
# encodeing：打开文件是的编码格式

# 路径分为两种：
# 1.绝对路径：从电脑盘符开始的路径
import os

# print(os.sep) # windows系统里，文件夹之间使用 \ 分隔。
# 在非windows系统里，文件夹之间使用 / 来分割

# 在python字符串里， \ 表示转义字符
# 绝对路径书写的三种方式：1.\\  2.r '\'     3.  '/'推荐
# file = open('D:\\python学习代码\\12-文件操作\\xxx.txt')
# file = open(r'D:\python学习代码\12-文件操作\xxx.txt',encoding='utf-8')
# file = open(r'D:/python学习代码/12-文件操作/xxx.txt',encoding='utf-8')



# 2.相对路径：当前文件所在的文件夹开始的路径。（用的多）
# ../表示返回到上一级文件夹
# ./可以省略不写，表示当前文件夹
# / 不能随便使用
file = open('xxx.txt',encoding='utf-8')
# file = open('./demo/sss.txt',encoding='utf-8') 下一级
# file = open('./../ppp.txt',encoding='utf8') 上一级


print(file.read())
file.close()
