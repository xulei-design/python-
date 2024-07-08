# 使用float内置类可以将其他类型数据转换成浮点数
a = '3.14'
b = float(a)
print(b + 1)

#如果字符串不能转换成为有效的浮点数，会报错。
# c = float('hello')
# print(c)

# c = 101
# print(float(c)) #101.0