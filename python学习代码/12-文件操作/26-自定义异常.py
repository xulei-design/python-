# 系统内置异常
# ZeroDivisionError：除以0的异常
# FileNotFoundError：文件不存在的异常
# FileExistsError:多次创建同名文件夹异常
# ValueError：int('hello')
# KeyError:字典中的键错误  person = {'name':'许磊'} person['age']
# SyntaxError: 语法错误
# IndexError:角标错误
# 要求：让用户输入用户名和密码，如果用户名和密码的长度在6~12 位正确，否则不正确
class Lengtherror(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须在{}和{}之间'.format(self.x, self.y)


password = input('请输入密码：')
m = 6
n = 12
if m <= len(password) <= n:
    print('密码正确')
else:
    # print('密码长度不正确，请重新输入')
    # 使用 raise 关键字可以抛出一个异常
    # raise ValueError('密码错误')
    raise Lengtherror(6, 12)

# 把密码保存到数据库中
print('把密码保存到数据库')
