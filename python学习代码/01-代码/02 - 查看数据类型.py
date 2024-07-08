a = 34
b = 'hello'
c = True
d = ['周杰伦','蔡徐坤','吴亦凡']
# 使用type内置可以查看一个变量对应的数据类型
print(type(a))
print(type(b))
print(type(c)) # type(c).print
print(type(d))
print(34)

# 在python中，变量是没有数据类型的，我们所说变量的数据类型，其实是变量对应值的数据类型，动态类型。
x = 34
print(type(x))
x = 3.14
print(type(x))