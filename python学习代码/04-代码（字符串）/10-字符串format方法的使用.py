# {} 也可以进行占位
# {} 什么都不写，会读取后面的内容，一一对应填充
x = '大家好，我是{}，我今年{}岁了'.format('张三', 18)
print(x)

# {数字} 根据数字的顺序进行填充。数字从 0 开始
y = '大家好，我是{1}，我今年{0}岁了'.format(19, '张三')
print(y)

# {变量名}
z = '大家好，我是{name}，我今年{age}岁了，我来自{addr}'.format(name='张三', age=18, addr="湖北")
print(z)

# 混合使用 {数字}  {变量名}
# 变量要写到最后面
a = '大家好，我是{1}，我来自{addr}，我的年龄是{0}'.format(18, '许磊', addr="河南")
print(a)

# {}什么都不写  {数字}不能混合使用

# 列表
d = ['zhangsan', 18, '上海', 180]
# b='大家好，我是{}，我今年{}岁了，我来自{}，我的身高是{}cm'.format(d[0],d[1],d[2],d[3])
b = '大家好，我是{}，我今年{}岁了，我来自{}，我的身高是{}cm'.format(*d)  # *d将列表拆分成字符串
print(b)


# 字典
info = {'name': 'chris', 'age': 23, 'addr': '北京', 'height': 190}
c = '大家好，我是{name}，我今年{age}岁了，我来自{addr}，我的体重是{height}'.format(**info)
print(c)
