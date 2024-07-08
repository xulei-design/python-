person={'name':'zhangsan','age':18,'x':'y'}

# 查找数据（字典在数据保存时，是无序的，不能通过下标来获取）
print(person['name']) # 使用 key 获取到对应的 value，
# print(person['height']) 如果查找的key不存在会报错
# key是唯一的，可以通过key找value,value是重复的，不能通过value找key

# 需求：获取一个不存在的key时，不报错，如果这个key不存在，使用默认值
# 使用字典的get方法,如果key不存在，会默认返回None,而不报错
# print(person.get('height')) # None
# 如果根据key获取不到value,使用给定的默认值
print(person.get('gender','female'))
print(person.get('name', 'zhangsan'))  #zhangsan

# print(person)

# print(person.get('age'))


# x = 'age'
# print(person[x])
# print(person['x'])





