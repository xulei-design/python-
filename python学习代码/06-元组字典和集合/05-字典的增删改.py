person = {'name': 'zhangsan', 'age': 18, 'height': 183}
print(person['name'])

# 直接使用key可以修改对应的value
person['name'] = 'lisi'
print(person)

# 如果key存在，修改对应的value;
# 如果key不存在，会往字典里添加一个新的key-value
person['gender'] = 'female'
print(person)
person['addr'] = '襄阳'
print(person)

# 把name对应的键值对删除
person.pop('name')
print(person)

# popitem 删除一个元素，结果是被删除的这个元素组成的键值对
result = person.popitem()
print(person) # {'age': 18, 'height': 183, 'gender': 'female'}
print(result) # print(result)


person.clear()  # 用来清空一个字典
print(person)  # {}

# del person['addr']
# print(person)