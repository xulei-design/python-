# 列表是用来保存多个数据的，是有序可变的
# 操作列表一般包括： 增加数据 删除数据 修改数据 查询数据
# 增删改查

heros = ['阿轲', '李元芳', '韩信', '嬴政', '后羿', '达摩', '亚瑟']

# 增加元素的方法 append insert extend
heros.append('黄忠')
print(heros) # 在列表的最后面追加一个数据

# insert(index,object) 需要两个参数
# index 表示下标，在哪个位置插入数据
# object 表示对象，具体插入那个数据
heros.insert(3,'李白') # 在指定位置插入数据
print(heros)

x = ['马可波罗','米莱迪','狄仁杰']
# extend (iterable) 需要一个可迭代对象
# A.extend(B) ==> 将可迭代对象 B 添加到 A 里
heros.extend(x)
print(heros)
print(x)