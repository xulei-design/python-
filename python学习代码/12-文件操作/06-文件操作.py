# python 里使用 open 内置函数用来打开一个文件
# file: 文件的路径，分为绝对路径和相对路径
# mode:打开文件模式。r:只读，w:写入， b:二进制（读取图片和视频）， t:文本形式打开
# mode:默认使用 rt
# encoding:用来指定文件的编码格式。windows系统里，默认是gbk

# file = open('xm.txt') # 报错，默认是rt,只读文件，文件不存在时会报错
# file = open('xm.txt','w',encoding='utf8') # 如果文件存在，会覆盖以前的内容，如果文件不存在时，会创建一个新的文件
# file.write('你好')

# file = open('xxx.txt', 'rt', encoding='utf8')
# print(file.read()) # 将所有的数据都读取出来
# print(file.readline()) #只读取一行
# readline只读取一行数据
# while True:
# #     content = file.readline()
# #     print(content)t
# #     if content == '':
# #         break

# 将所有行的数据读取，保存到一个列表里
# x = file.readlines()
# print(x)


# x = file.read(1024) # 指的是读取的长度
# print(x)


# 优化：没有绝对的优化，除非提升硬件
# 软件层面：时间  /  空间
# file.close()


file_name = './demo/sss.txt'
with open(file_name,'r',encoding='utf8') as file_object:
    file_list = file_object.readlines()
print(file_list)
for line in file_list:
    print(line.rstrip())