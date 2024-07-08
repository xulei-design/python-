# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]
# nums.sort()
# print(nums)


# sorted 内置函数，不会改变原有的数据，而是生成一个新的有序列表
x = sorted(nums)
print(x)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 173}
]


# 字典和字典之间不能使用比较运算
# students.sort()

# foo这个函数需要0个位置参数，但是在调用时传递了一个参数
def foo(ele):
    print('ele={}'.format(ele))
    return ele['age'] # 通过返回值告诉sort方法，按照元素的哪个属性进行排序


# 需要传递参数  key 指定比较规则
# key参数类型是一个函数
# 在sort内部实现时，调用了foo方法，并且传入了一个参数，参数就是列表里的元素
students.sort(key=foo) #None
print(type(foo))

# students.sort(key=lambda ele:ele['age'])
print(students)
