person = {'name': 'zhangsan', 'age': 18, 'height': 183}

# 特殊在列表和元组是一个单一的数据，但字典是键值对的形式

# 第一种遍历方式(字典是可迭代对象）
# for x in person:  # for...in循环获取到的是key
#     print(x, '=', person[x])

# 第二种方式：获取到所有的key,然后遍历key,根据key获取value
# print(person.keys()) # dict_keys(['name', 'age', 'height'])
# for k in person.keys():
#     print(k,'=',person[k])


# 第三种方式：只获取到所有的value

# for v in person.values():
#     print(v)


# 第四种遍历方式：
# print(person.items()) # dict_items([('name', 'zhangsan'), ('age', 18), ('height', 183)])

# for item in person.items():  # 列表里的元素是元组，把元组当作整体进行遍历
#     print(item) # 获取到一个个的元组，item 是元组
#     print(item[0], '=', item[1])


for k, v in person.items():
    print(k, '=', v)
