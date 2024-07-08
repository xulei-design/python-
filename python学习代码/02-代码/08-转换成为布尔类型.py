# 使用bool内置类可以将其他数据类型转换成为布尔值
print(bool(100))# 将数字100转换成布尔值 True
print(bool(-1))#-1转换成布尔值也是 True
print(bool(0)) #Flase

# 数字里，只有数字0转换成布尔值是Flase,其他数字转换成布尔值都是True
#在python中，只有空字符串'',""，数字0,空字典{},空列表[],空元组(),
# 和空数据None会被转换成为False,其他的都会被转换成为True


print(bool('hello'))#True 1
print(bool('')) #Flase
print(bool(None))

# 隐式类型转换
if 3>2:
    print('hello')
if 3:
    print('good')
if 0:
    print('nice')