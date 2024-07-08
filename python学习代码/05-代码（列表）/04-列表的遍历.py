# 遍历：将所有的数据都访问一遍。遍历针对的是可迭代对象
# while循环遍历  / for...in 循环遍历
killers = ['李白', '兰陵王', '阿轲', '孙悟空', '赵云', '韩信', '百里玄策']

# for...in 循环的本质是不断调用迭代器的 next 方法查找下一个数据
for killer in killers:
    print(killer)


# while 循环遍历
# len() 长度查找适用于字符串和列表
i = 0
while i < len(killers):
    print(killers[i])
    i += 1
