# with
# try:
#     file = open('dog.txt','r')
# except FileNotFoundError:
#     print('文件不存在')
# else:
#     try:
#         file.read()
#     finally:
#         file.close()
# x = open('01-打开文件.py','r',encoding='utf8')
# print(type(x))  # <class '_io.TextIOWrapper'>

try:
    with open('01-打开文件.py','r',encoding='utf8') as file:
        file.read() #不需要再手动关闭文件
        # file.close() with关键字会帮助我们关闭文件
except FileNotFoundError:
    print('文件不存在')

# with 我们称之为上下文管理器，很多需要手动关闭的链接
# 比如说：文件链接，scoket连接，数据库连接，都能够使用with关键字自动关闭连接
# with 关键字后面对象，需要实现 ___enter__ 和 __exit__ 这两个魔法方法
