# 在python里，可以使用一对单引号，双引号或者一对三个双引号，一对三个单引号
a = 'hello'
b = "good"
c = """呵呵呵"""
d = '''嘿嘿嘿'''

# 如果字符串里含有双引号（单引号），外面就可以使用单引号（双引号）
m = 'xiao ming said :"Im xiao ming" '
n = "I'm xiaoming"
c = """xiaoming said :"I am xiaoming" """

# 字符串的转义字符
# \' ==> 显示一个普通的单引号
# \" ==> 显示一个普通的双引号
# \n ==> 表示一个换行
# \t ==> 表示显示一个制表符（空四个空格）
# \\ ==> 表示一个普通的反斜线
# 在字符串的前面添加 r 在python里表示原生字符串
x = 'I\'m xiaoming' # \ 表示的是转义字符，作用是对 \ 后面的字符进行转义
y = "xiaoming said:\"I am xiaoming\""
z = 'hello \n world'
print(y)
print(z)

x1 = '你好\t世界'
print(x1)

x2 = 'good mor\\ning'
print(x2)

# 在字符串的前面添加 r 在python里表示原生字符串
x3 = r'hello \teacher'
print(x3)
# hello \teacher