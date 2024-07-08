# python 里的for循环指的是for...in 循环。
# for 语句格式：for ele in iterable

# range 内置类用来生成指定的区间序列(列表)
# 注意： in 的后面必须是一个可迭代对象！！！
# 目前接触的可迭代对象：字符串，列表，字典，元组，集合，range
for i in range(1,11): #左开右闭
    print(i)
    #等同
for x in [1,2,3,4,5,6,7,8,9,10]:# 便利操作，逐个取出
    print(x)

for y in 'hello':
    print(y)
# for m in 10:
#     print(m)
sum = 0 # 定义一个变量，保存所有的数字之和
for m in range(1 , 101):
    sum = sum + m
print(sum)