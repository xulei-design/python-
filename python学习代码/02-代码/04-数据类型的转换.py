# 类型转换：将一个类型转换为其它类型的数据
#int==> str      str==> int     bool==>int     int==> float

# age = input('请输入你的年龄：')
# print(type(age))
#print(age + 1) 报错15
#原因：input 接受的用户输入都是str字符串类型
#在python中，不同数据类型之间不能作运算
# new_age = int(age) # 使用int 内置类可以将其他类型的数据转换为整数。
# print(type(new_age))
# print(new_age+1)


# a = '31'
# b = int(a)
# print(a+1) #报错，字符串与数字不能运算
# print(b+1)  # 32


# str1 = str(45)
# str2 = str(34.56)
# str3 = str(True)
# print(type(str1),type(str2),type(str3))

# 如果字符串不是一个合法的数字，会报错
# x = 'hello'
# y = int(x)
# print(y)


m = '12'
y = int(m,8) # 把字符串12当作八进制转换为整数
print(y)  #10