# 内置类 list tuple set
nums = [5, 8, 7, 6, 4, 1, 3, 5, 7, 8, 4]
x = tuple(nums)  # 使用tuple内置类转换成元组
print(x)

y = set(x)  # 使用set内置类转换成集合
print(y)

z = list({'name': 'zhangsan', 'age': 18, 'score': 98})  # 在对字典进行转换时只转换key
print(z)

# python里有一个比较强大的内置函数eval，可以执行字符串里的代码
# a = 'input("请输入你的用户名：")'  # a是一个字符串
# eval(a)
b = '1+1'
print(b)
print(eval(b))

import json

# JSON的使用，把列表，元组，字典等转换成为JSON字符串
# JSON里的字符串只能用双引号
person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}
# 字典如果想要把它传入前端页面，或者把字典写入到一个文件中，要将其数据类型的转换成为JSON字符串
# '{"name": "zhangsan", "age": 18, "gender": "female"}'
m = json.dumps(person)  # dump将字典，列表，集合，元组，等转换成为JSON字符串
print(m)
# print(type(m))


# python            JSON
# 字符串             字符串
# 字典                对象
# 列表，元组          数组
# True              true
# False            false

# 列表元组字典集合都是可迭代对象
# 可以使用内置函数eval或则loads可以将JSON字符串转换成为python里的数据
n = '{"name": "zhangsan", "age": 18, "gender": "female"}'
# p = eval(n)
# print(p)
# print(type(p))
s=json.loads(n)
print(s)
print(type(s))