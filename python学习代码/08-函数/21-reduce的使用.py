from functools import reduce  # 导入模块语法


# reduce以前是一个内置函数
# 内置函数和内置类都在 builtins.py 文件中  c内置类 f内置函数

def foo(x, y):  # x =100 y=92  x=192 y=85
    return x + y


scores = [100, 92, 85, 74, 98]
print(reduce(foo, scores))
print(type(reduce))
# 使用reduce求所有学生的总年龄
students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 173}
]

# def sum_ages(x, y):
#     # x={'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180}  y={'name': 'lisi', 'age': 21, 'score': 97, 'height': 185}
#     # x=0 y=18   x=18 y=12
#     return x + y['age']
# y整个字典'age'的值


# 指定初始化的值
# reduce 减项加法
# x = reduce(sum_ages,students,0)
# print(x)


m = reduce(lambda x, y: x + y['age'], students, 0)
print(m)
