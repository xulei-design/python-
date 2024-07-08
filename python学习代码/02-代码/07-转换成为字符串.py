#使用 str 内置类将其他类型数据转换成为字符串类型
a = 15
b = str(a)
print(type(a))#<class 'int'>
print(type(b))#<class 'str'>
print(a) #15
print(b) #15
print(a + 1) #16
print(b + 1) #报错