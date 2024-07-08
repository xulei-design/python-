a = 13
b = 20

# 方法一：引用第三方变量实现
# c = a
# a = b
# b = c

# 方法二：使用运算符来实现，只能是数字
a = a + b
b = a - b
a = a - b

# 方法三： 使用异或运算符
a = a ^ b
b = a ^ b
a = a ^ b
# 原理： a ^ b ^ b ==> a


# 方法四：使用python特有的
a, b = b, a

print(a)  # 20
print(b)  # 13
