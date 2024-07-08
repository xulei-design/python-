# python 里使用 open 内置函数打开并操作一个文件

# open 参数介绍
# file:用来指定打开的文件（不是文件的名字，而是文件的路径）
# mode：打开文件的模式，默认是 r 表示只读
# encodeing：打开文件是的编码格式

# open函数会有一个返回值
# xxx.txt 写入时，使用utf-8编码格式
# 在windows操作系统中，默认使用gbk编码格式
file = open('xxx.txt', 'r',encoding='utf8')
# print(type(file))
print(file.read())

# 操作完成以后，关闭文件
file.close()