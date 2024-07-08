# 集合是一个不重复的无序，可以使用{}或则 set 来表示
# {} 有两种意思：字典 ，集合
# {} 里如果放键值对，他就是一个字典；如果{}放的是单个的值，就是一个集合
person = {'name': 'zhangsan', 'age': 18} # 字典
x = {'hello', 1, 'good'} # 集合

# 如果集合有重复的数据，会自动去除重复数据
names = {'zhangsan','lisi','jack','tony','lisi','赵四'}
print(names)


# set能不能增删改查
names.add('阿轲') # 集合元素的添加
print(names)

#空集合的表示方式不是{}，{}表示空字典
#空集合的表示方式 set()
# names.clear() # 清空一个集合
# print(names)

names.pop() # 随即删除一个元素
print(names)

names.remove('tony')# 删除指定元素
print(names)

# union 取两个集合的并集，生成一个新的集合
print(names.union({'刘能', '赵四', '阿轲'}))
print(names)

# A.update(B) 将B拼接到A里面
names.update({'刘能','赵四'})
print(names)