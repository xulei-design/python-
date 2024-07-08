# filter 对可迭代对象进行过滤,得到的是一个filter对象
# pyton2的时候是内置函数，python3修改成了一个内置类

ages = [12, 18, 19, 24, 21, 16]
# filter可以给定两个参数，第一个参数是函数，第二个参数是一个可迭代对象
# filter结果是一个filter类型的对象，filter对象也是一个可迭代对象
x = filter(lambda ele: ele > 18, ages)
# print(x)  # <filter object at 0x0000016CDDA7DBC8> 面型对象
# for a in x:
#     print(a)

adult = list(x)
print(adult) # [19, 24, 21]