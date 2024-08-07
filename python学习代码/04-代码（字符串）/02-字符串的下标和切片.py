# 下标我们又称之为索引，表示第几个数据

# 可迭代对象：字符串str list tuple dict set range 都可以便利
# str list tuple 可以通过下标来获取或者操作数据

# 在计算机里，下标都是从0开始的。
word = 'zhangsan'  # 字符串：一个一个的字符串在一起
# 可以通过下标来获取或者修改指定位置的数据
print(word[4])

# 字符串是不可变数据类型
# 对于字符串的任何操作，都不会改变原有的字符串！！！
if word[4] == 'g':
    print('1')
else:
    print('0')

# 切片就是从字符串里复制一段内容，生成一个新的字符串
m = 'abcdefghijklmnopqrstuvwxyz'
print(m[5])  # m[index] ==> 获取指定下标的数据
# 切片语法  m[start:end:step]
# 包含start,不包含end
# step 指的是步长，理解为间隔。每隔 step-1 个取一次

print(m[2:9])  # cdefghi #包含start,不包含end
print(m[2:])  # 如果只设置了start,会“截取”到最后
print(m[:9])  # 如果只设置了end,会从头开始“截取”。
print(m[3:15:2])  # defghijklmno  #dfhjln
print(m[3:15:1])  # defghijklmno
# print(m[3:15:0])  步长不能为0
print('--------------')
print(m[3:15])
print(m[3:15:1])  # 没有数据
print(m[15:3:-1])  # ponmlkjihgfe
print(m[::])  # abcdefghijklmnopqrstuvwxyz 从头到尾复制
print(m[::-1])  # zyxwvutsrqponmlkjihgfedcba

print(m[-9:-5])  # rstu
