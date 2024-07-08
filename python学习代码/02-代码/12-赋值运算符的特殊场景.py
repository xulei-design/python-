# 等号变量可以传递赋值
a = b = c = d = 'hello'
print(a, b, c, d)

# x = 'yes' = y = z
m, n =[15, 20]   #拆包 列表
print( m, n)

x = 'hello' ,'world','yes' #元组
print(x) #('hello', 'world', 'yes')

# 拆包时，变量的个数和值的个数不一致时会报错
# y, z = 1, 2, 3, 4, 5   报错
# print(y, z)

#o, p, q = 4, 2
# print(o, p, q)

o, *p, q = 1, 2, 3, 4, 5, 6  # *代表可变长度
print(o, p, q) # 1 [2, 3, 4, 5] 6

o, p, *q = 1, 2, 3, 4, 5, 6  # *代表可变长度
print(o, p, q)  # 1 2 [3, 4, 5, 6]